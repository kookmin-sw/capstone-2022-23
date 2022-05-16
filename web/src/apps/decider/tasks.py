from __future__ import absolute_import, unicode_literals
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
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


@shared_task
# def crawl(url):
def crawl():
    url = "https://blog.daum.net/9855/79"
    header = {
        "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=header)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "html.parser")

    images = soup.find_all("img")

    for i, img in enumerate(images):
        src = img.get("src")
        if src == None:
            continue
        if not src.startswith("http"):
            continue
        if src.endswith(".svg") or ".gif" in src:
            continue

        res = requests.get(src)

        img = Image.open(BytesIO(res.content))
        img = img.convert("RGB")
        img = img.resize((64, 64))
        data = np.asarray(img)
        X = np.array(data)
        X = X.astype("float") / 256
        X = X.reshape(-1, 64, 64, 3)

    return X


@shared_task
def get_tokenized():
    with open("apps/decider/TokenafterSentence.pickle", "rb") as f:
        list_ex = pickle.load(f)

    kkma = Kkma()
    tokenizer = Tokenizer(19845)
    tokenizer.fit_on_texts(list_ex)
    # only_text = crawl()

    only_text = "test.테스트"
    tokens = kkma.sentences(only_text)
    return tokens, tokenizer


@shared_task
def mul(x, y):
    return x * y
