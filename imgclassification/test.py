import json
import requests
from PIL import Image
import numpy as np

categories = ["anger","fear","joy","love","sadness","surprise"]

test_image = './testimg_sadness2.jpg'
# 이미지 resize
img = Image.open(test_image)
img = img.convert("RGB")
img = img.resize((64,64))
data = np.asarray(img)
X = np.array(data)
X = X.astype("float") / 256
X = X.reshape(-1, 64, 64,3)

address = 'http://localhost:8501/v1/models/resnet152:predict'
data = json.dumps({'instances':X.tolist()})

result = requests.post(address, data=data)
predictions = json.loads(str(result.content, 'utf-8'))['predictions']

for prediction in predictions:
  print(np.argmax(prediction))
  print('New data category : ',categories[np.argmax(prediction)])