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

TENSER_SERVING_URL = "http://mooddecider.com:8501/v1/models/LSTM:predict"


# @shared_task
# def crawl(url):
# def crawl():
#     url = "https://blog.daum.net/9855/79"
#     header = {
#         "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
#     }
#     req = urllib.request.Request(url=url, headers=header)
#     html_page = urlopen(req)

#     soup = BeautifulSoup(html_page, "html.parser")

#     images = soup.find_all("img")

#     for i, img in enumerate(images):
#         src = img.get("src")
#         if src == None:
#             continue
#         if not src.startswith("http"):
#             continue
#         if src.endswith(".svg") or ".gif" in src:
#             continue

#         res = requests.get(src)

#         img = Image.open(BytesIO(res.content))
#         img = img.convert("RGB")
#         img = img.resize((64, 64))
#         data = np.asarray(img)
#         X = np.array(data)
#         X = X.astype("float") / 256
#         X = X.reshape(-1, 64, 64, 3)

#     return X

@shared_task
def trigger(user, site):
    only_text = get_mood(site.url)
    qs = Result.objects.get(url=site, user=user)
    qs.status = 'completion'
    qs.mood = only_text
    qs.save()
    
    
@shared_task
def get_tokenized(only_text):
    with open("TokenafterSentence.pickle", "rb") as f:
        list_example = pickle.load(f)

    kkma = Kkma()
    tokenizer = Tokenizer(19845)
    tokenizer.fit_on_texts(list_example)

    tokens = kkma.sentences(only_text)
    return tokens, tokenizer

@shared_task
def crawl(url: str) -> str:
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    only_text = soup.get_text()
    return only_text

@shared_task
def get_mood(url: str) -> str:
    only_text = crawl(url)
    tokens, tokenizer = get_tokenized(only_text)
    top_three = [0 for _ in range(13)]

    for token in tokens:
        sequences = tokenizer.texts_to_sequences([token])

        if not sequences[0]:
            continue

        data = json.dumps({"instances": sequences})

        result = requests.post(url=TENSER_SERVING_URL, data=data)
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

    # context = {
    #     "token": emotions[np.argmax(top_three)],
    # }
    
    return emotions[np.argmax(top_three)]
    # return render(request, "decider.html", context=context)

# @shared_task
# def get_mood():
#     kkma = Kkma()
#     url = "https://blog.daum.net/9855/79"
#     res = req.urlopen(url).read()
#     html = urlopen(url).read()
#     with open("TokenafterSentence.pickle", "rb") as f:
#         list_ex = pickle.load(f)

#     tokenizer = Tokenizer(19845)
#     tokenizer.fit_on_texts(list_ex)
#     address = "http://mooddecider.com:8501/v1/models/LSTM:predict"
#     bsObject = BeautifulSoup(html, "html.parser")
#     onlytext = bsObject.get_text()
    # token = kkma.sentences(onlytext)
    # strlist = []
    # topthree = [0 for i in range(13)]
    # for i in token:
    #     strlist.append(i)
    #     x_list = tokenizer.texts_to_sequences(strlist)
    #     strlist.clear()
    #     if len(x_list[0]) == 0:
    #         continue
    #     data = json.dumps({"instances": x_list})
    #     result = requests.post(address, data=data)
    #     # print(result)
    #     predictions = json.loads(str(result.content, "utf-8"))["predictions"]
    #     lyric_emotion = [
    #         "성적",
    #         "기쁨",
    #         "두려움",
    #         "환상",
    #         "반항",
    #         "불안",
    #         "승리",
    #         "재미",
    #         "아름다움",
    #         "이별",
    #         "짜증",
    #         "편안",
    #         "활력",
    #     ]
    #     for prediction in predictions:
    #         # print(lyric_emotion[np.argmax(prediction)])
    #         topthree[np.argmax(prediction)] += 1
    # # print(topthree)
    # sortlist = sorted(topthree)
    # # print(sortlist)
    # print("######################################")
    # print(topthree.index(sortlist[-1]) + 1)
    # return return_results(lyric_emotion[topthree.index(sortlist[-1])])
    # return onlytext


@shared_task
def mul(x, y):
    return x * y
