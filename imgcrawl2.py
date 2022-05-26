from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import json

def crawl(url: str):
    image_list = []
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    only_text = soup.get_text()

    images = soup.find_all('img')

    for i, img in enumerate(images):
        src = img.get('src')
        #print(src)
        if src == None:
            continue
        if not src.startswith('http'):
            continue
        if src.endswith('.svg') or '.gif' in src:
            continue

        result = requests.get(src)

        img = Image.open(BytesIO(result.content))
        img = img.convert("RGB")
        img = img.resize((64,64))
        data = np.asarray(img)
        data = np.array(data)
        data = data.astype("float") / 256
        data = data.reshape(-1, 64, 64,3)

        image_list.append(data)

    return only_text, image_list

def get_mood_from_image(url: str):
    _, image_list = crawl(url)
    categories = ["anger","fear","joy","love","sadness","surprise"]
    result_list = [0, 0, 0, 0, 0, 0]

    if not image_list:
        print("No image")
        return

    for img in image_list:
        address = 'http://localhost:8501/v1/models/resnet152:predict'
        data = json.dumps({'instances':img.tolist()})

        result = requests.post(address, data=data)
        predictions = json.loads(str(result.content, 'utf-8'))['predictions']

        for prediction in predictions:
            #print('New data category : ',categories[np.argmax(prediction)])
            result_list[np.argmax(prediction)] += 1

    print(categories[np.argmax(result_list)])
    



