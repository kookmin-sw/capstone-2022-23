from __future__ import absolute_import, unicode_literals
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request as req
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import nltk
import pickle5 as pickle
from konlpy.tag import Kkma
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from tensorflow.keras.preprocessing.text import Tokenizer
import json
from .models import Result, Site

TENSER_SERVING_LSTM_URL = "http://mooddecider.com:8501/v1/models/LSTM:predict"
TENSER_SERVING_IMGCLASS_URL = "http://mooddecider.com:8501/v1/models/IMGCLASS:predict"


@shared_task
def trigger(user, site):
    text_mood, image_mood = get_mood(site.url)
    result = Result.objects.get(url=site, user=user)
    result.status = "completion"
    if text_mood != None and image_mood != None:  # image_mood , text_mood 값이 모두 존재할 경우
        result.text_mood = text_mood
        result.image_mood = image_mood
    elif text_mood == None and image_mood == None:  # image_mood, text_mood 값이 모두 없을 경우
        result.status = "failure"
    elif text_mood != None:  # text_mood 값이 있을 경우
        result.text_mood = text_mood
        result.image_mood = "분석 실패"
    else:
        result.text_mood = "분석 실패"
        result.image_mood = image_mood
    result.save()


@shared_task
def get_mood_from_text(text_list):
    try:
        tokens, tokenizer = get_tokenized(text_list)
        top_three = [0 for _ in range(13)]

        for token in tokens:
            sequences = tokenizer.texts_to_sequences([token])

            if not sequences[0]:
                continue

            data = json.dumps({"instances": sequences})

            result = requests.post(url=TENSER_SERVING_LSTM_URL, data=data)
            predictions = json.loads(str(result.content, "utf-8"))["predictions"]

            # 순서에 유의
            emotions = [
                "성적",
                "기쁨",
                "두려움",
                "환상",
                "반항",
                "불안",
                "승리",
                "재미",
                "아름다움",
                "이별",
                "짜증",
                "편안",
                "활력",
            ]

            for prediction in predictions:
                top_three[np.argmax(prediction)] += 1

        text_mood = emotions[np.argmax(top_three)]
        return text_mood
    except Exception as e:
        print(e)


@shared_task
def get_mood(url):
    text_list, image_list = crawl(url)

    text_mood = get_mood_from_text(text_list)
    image_mood = get_mood_from_image(image_list)

    return text_mood, image_mood


@shared_task
def crawl(url: str):
    image_list = []
    text_list = []

    try:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        text_list = soup.get_text()

        images = soup.find_all("img")

        for image in images:
            src = image.get("src")

            if src == None:
                continue
            if not src.startswith("http"):
                continue
            if src.endswith(".svg") or ".gif" in src:
                continue

            result = requests.get(src)

            byte_image = Image.open(BytesIO(result.content))
            byte_image = byte_image.convert("RGB")
            byte_image = byte_image.resize((64, 64))

            data = np.asarray(byte_image)
            data = np.array(data)
            data = data.astype("float") / 256
            data = data.reshape(-1, 64, 64, 3)

            image_list.append(data)

    except Exception as e:
        print(e)

    return text_list, image_list


def get_mood_from_image(image_list):
    try:
        categories = ["anger", "fear", "joy", "love", "sadness", "surprise"]
        result_list = [0, 0, 0, 0, 0, 0]

        for img in image_list:
            data = json.dumps({"instances": img.tolist()})

            result = requests.post(TENSER_SERVING_IMGCLASS_URL, data=data)
            predictions = json.loads(str(result.content, "utf-8"))["predictions"]

            for prediction in predictions:
                # print('New data category : ',categories[np.argmax(prediction)])
                result_list[np.argmax(prediction)] += 1

        image_mood = categories[np.argmax(result_list)]
        return image_mood
    except Exception as e:
        print(e)


@shared_task
def get_tokenized(text_list):
    with open("TokenafterSentence.pickle", "rb") as f:
        list_example = pickle.load(f)

    kkma = Kkma()
    tokenizer = Tokenizer(19845)
    tokenizer.fit_on_texts(list_example)

    tokens = kkma.sentences(text_list)
    return tokens, tokenizer


# @shared_task
# def crawl(url):
#     html = urlopen(url).read()
#     soup = BeautifulSoup(html, "html.parser")
#     text_list = soup.get_text()
#     return text_list
