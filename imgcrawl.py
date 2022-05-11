from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
from PIL import Image
from io import BytesIO
import numpy as np
import requests

hdr={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.google.com/search?q=google&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjTsKT5xdf3AhWUBt4KHRfDACcQ_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1"
req=urllib.request.Request(url=url, headers=hdr)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, 'lxml')

images = soup.find_all('img')

for i, img in enumerate(images):
    src = img.get('src')
    print(src)
    if src == None:
        continue
    """if not src.startswith('http'):
        continue"""
    if src.endswith('svg'):
        continue


    res = requests.get(src)

    img = Image.open(BytesIO(res.content))
    img = img.convert("RGB")
    img = img.resize((64,64))
    data = np.asarray(img)
    X = np.array(data)
    X = X.astype("float") / 256
    X = X.reshape(-1, 64, 64,3)

    print(X)
    



