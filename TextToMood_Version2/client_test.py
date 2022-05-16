import json
import requests
import numpy as np










#8. 모델을 불러와 test를 진행합니다. 
from typing import Sequence
import keras 
from keras.layers import LSTM, Dropout,  Dense
from konlpy.tag import Kkma
from keras.preprocessing import sequence
from keras.utils import  np_utils
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pandas as pd
import pickle
import os
import nltk
import tensorflow as tf
def tokenize_sentense(text): #토큰화를 진행합니다.
    kkma = Kkma()
    return kkma.pos(text)
with open("TokenafterSentence.pickle","rb") as f:
    list_ex = pickle.load(f)
def removepos(token): #해당 단어에서 불용어를 처리합니다.
    result = []
    for index in range(len(token)):
        word,tag = token[index]
        if tag in 'SF' or tag in 'SP' or tag in 'SS' or tag in 'SE' or tag in 'SO' or tag in 'SW'  or tag in 'ON':
            continue      
        else:
            result.append(word)
    return result






tokenizer = Tokenizer(19845)
tokenizer.fit_on_texts(list_ex)
#test 예제
test = "난 괜찮을 것이라고 다짐했어. 하지만 결국엔 하염없이 눈물이 나오고 말았지. 더는 참을 수 없을 때 이런 눈물을 통해 마음이 조금은 깨끗해지고 평온해지기만을 바랄 뿐이야. "
test2 = "너처럼 웃어 주는 나 눈을 떴을 때 있던 네 가 이젠 눈을 감아야지"
strlist = []
strlist2 = []
strlist.append(test)
strlist2.append(test2)
strlistlist =[]
strlistlist.append(strlist)
strlistlist.append(strlist2)
x_list = tokenizer.texts_to_sequences(strlistlist)
x_list2 = tokenizer.texts_to_sequences(removepos(tokenize_sentense(test2)))
print(x_list)
print(x_list2)
# xx_list = []
# xx_list.append(x_list)
# xx_list.append(x_list2)
# y_prob = new_model.predict(x_list,verbose =0)
# print(type(y_prob))
# predicted = y_prob.argmax(axis=-1)
# print(predicted)

# lyric_emotion = ['슬픔', '부정', '분노', '무관심']
# print(lyric_emotion[y_prob.sum(axis=0).argmax()]) #가장 점수가 높은 감정이 추출됩니다.










# # test_image = Image.open('test_image.jpg')
# pixels = np.array(test_image)/255.0

address = 'http://localhost:8501/v1/models/LSTM:predict'

data = json.dumps({'instances':x_list})

result = requests.post(address, data=data)
print(result)
predictions = json.loads(str(result.content, 'utf-8'))['predictions']


lyric_emotion = ['성적', '기쁨', '두려움', '환상','반항','불안','승리','재미','아름다움','이별','짜증','편안','활력']
# print(predictions)
for prediction in predictions:
    print(lyric_emotion[np.argmax(prediction)])

# for prediction in predictions:
#   print(np.argmax(prediction))