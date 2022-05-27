from bs4 import BeautifulSoup
from urllib.request import urlopen
#import urllib.request
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import json
import pickle
import collections
import cv2

def manhattan_distance(x, y): #manhattan distance
    return sum(abs(a-b) for a,b in zip(x,y))

with open("D:/capstone-2022-23/img/dict/angry_dict.pkl", 'rb') as f:
    angry_dict = pickle.load(f)
with open("D:/capstone-2022-23/img/dict/fear_dict.pkl", 'rb') as f:
    fear_dict = pickle.load(f)
with open("D:/capstone-2022-23/img/dict/joy_dict.pkl", 'rb') as f:
    joy_dict = pickle.load(f)
with open("D:/capstone-2022-23/img/dict/love_dict.pkl", 'rb') as f:
    love_dict = pickle.load(f)
with open("D:/capstone-2022-23/img/dict/sadness_dict.pkl", 'rb') as f:
    sadness_dict = pickle.load(f)
with open("D:/capstone-2022-23/img/dict/surprise_dict.pkl", 'rb') as f:
    surprise_dict = pickle.load(f)

psycolors = [[255,0,0], [255,165,0], [255,255,0], [0,128,0], [0,0,255], [75,0,130], [128,0,128], [64,224,208], [255,192,203], [255,0,255], [165,42,42], [128,128,128], [192,192,192], [255,215,0], [255,255,255], [0,0,0]]
categories = ["anger","fear","joy","love","sadness","surprise"]
result_list = [0, 0, 0, 0, 0, 0]

#hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://mygoodplace.tistory.com/51?category=995448"
#req=urllib.request.Request(url=url, headers=hdr)
html_page = urlopen(url).read()

soup = BeautifulSoup(html_page, 'html.parser')

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

    res = requests.get(src)

    img = Image.open(BytesIO(res.content))
    img = img.convert("RGB")
    data_for_kmeans = np.asarray(img).reshape(-1, 3).astype(np.float32)
    #print(data_for_kmeans)
    img = img.resize((64,64))
    data = np.asarray(img)
    X = np.array(data)
    X = X.astype("float") / 256
    X = X.reshape(-1, 64, 64,3)

    criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10, 0.001)
    retval, bestLabels, centers = cv2.kmeans(data_for_kmeans, 7, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    centers = centers.astype(np.uint8)
    clustered_data = centers[bestLabels].reshape(data_for_kmeans.shape)

    counts = collections.Counter(map(tuple, clustered_data))

    combi = [counts.most_common(2)[0][0], counts.most_common(2)[1][0]]
    #print(combi)

    for i in range(2):
        min = 999999
        for j in range(len(psycolors)):
            md = manhattan_distance(combi[i], psycolors[j])
            if md < min:
                min = md
                temp = psycolors[j]
        combi[i] = tuple(temp)

    combi = tuple(combi)
    #print(combi)

    address = 'http://localhost:8501/v1/models/IMGCLASS:predict'
    data = json.dumps({'instances':X.tolist()})
    
    result = requests.post(address, data=data)
    predictions = json.loads(str(result.content, 'utf-8'))['predictions']

    for prediction in predictions:
        prediction = np.log(prediction)

        prediction[0] = prediction[0] * np.log(sum(angry_dict.values())/angry_dict.get(combi, 0.1))
        prediction[1] = prediction[1] * np.log(sum(fear_dict.values())/fear_dict.get(combi, 0.1))
        prediction[2] = prediction[2] * np.log(sum(joy_dict.values())/joy_dict.get(combi, 0.1))
        prediction[3] = prediction[3] * np.log(sum(love_dict.values())/love_dict.get(combi, 0.1))
        prediction[4] = prediction[4] * np.log(sum(sadness_dict.values())/sadness_dict.get(combi, 0.1))
        prediction[5] = prediction[5] * np.log(sum(surprise_dict.values())/surprise_dict.get(combi, 0.1))

        print('New data category : ',categories[np.argmax(prediction)])
        result_list[np.argmax(prediction)] += 1

print(categories[np.argmax(result_list)])
    



