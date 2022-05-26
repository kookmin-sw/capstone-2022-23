from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
from PIL import Image
from io import BytesIO
import numpy as np
import requests
import json
import time

categories = ["anger","fear","joy","love","sadness","surprise"]
result_list = [0, 0, 0, 0, 0, 0]

#hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://mygoodplace.tistory.com/64"
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
    img = img.resize((64,64))
    data = np.asarray(img)
    X = np.array(data)
    X = X.astype("float") / 256
    X = X.reshape(-1, 64, 64,3)

    address = 'http://localhost:8501/v1/models/IMGCLASS:predict'
    data = json.dumps({'instances':X.tolist()})
    print(X.tolist()[0][0][0][:10])
    
    result = requests.post(address, data=data)
    predictions = json.loads(str(result.content, 'utf-8'))['predictions']

    for prediction in predictions:
        print('New data category : ',categories[np.argmax(prediction)])
        result_list[np.argmax(prediction)] += 1

print(categories[np.argmax(result_list)])
    



