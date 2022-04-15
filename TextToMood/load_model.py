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
def tokenize_sentense(text):
    kkma = Kkma()
    return kkma.pos(text)
with open("TokenafterSentence.pickle","rb") as f:
    list_ex = pickle.load(f)
def removepos(token):
    result = []
    for index in range(len(token)):
        word,tag = token[index]
        if tag in 'SF' or tag in 'SP' or tag in 'SS' or tag in 'SE' or tag in 'SO' or tag in 'SW'  or tag in 'ON':
            continue      
        else:
            result.append(word)
    return result

def word2num(list_2d): #단어들을 리스트에 숫자를 넘어 지정해줍니다.
    w2n_dic = dict()
    n2w_dic = dict()
    idx = 1
    num_list = [[]for _ in range(len(list_2d))]
    for k, i in enumerate(list_2d):
        if not i:
            continue
        elif isinstance(i, str):
            #내용이 단어 하나로 이루어진 경우, for loop으로 ['단어']가 '단'과 '어'로 나뉘지 않게 한다.
            if w2n_dic.get(i) is None:
                w2n_dic[i] =idx
                n2w_dic[idx] = i
                idx += 1

            num_list[k] = [w2n_dic[i]]
        else:
            for j in i:
                if w2n_dic.get(j) is None:
                    w2n_dic[j] = idx
                    n2w_dic[idx] = j
                    idx+=1
                num_list[k].append(w2n_dic[j])
    return num_list, w2n_dic, n2w_dic


def divide_data(x, y, train_prop = 0.8): #8대 2의 비율로 데이터를 분할하여 데이터 셋을 생성합니다.
    x = np.array(x)
    y = np.array(y)
    tmp = np.random.permutation(np.arange(len(x)))
    x_tr = x[tmp][:round(train_prop * len(x))]
    y_tr = y[tmp][:round(train_prop*len(x))]
    x_te = x[tmp][-(len(x)-round(train_prop*len(x))):]
    y_te = y[tmp][-(len(x)-round(train_prop * len(x))):]
    return x_tr, x_te, y_tr, y_te
new_model = tf.keras.models.load_model('musicdecider') #만들어진 lstm 모델을 불러옵니다.


tokenizer = Tokenizer(11295)
tokenizer.fit_on_texts(list_ex)
# tokenizer.fit_on_texts(list_ex)

# test = "니 뭐하나 지금"
# print(tokenize_sentense(test))

test = "난 괜찮을 것이라고 다짐했어. 하지만 결국엔 하염없이 눈물이 나오고 말았지. 더는 참을 수 없을 때 이런 눈물을 통해 마음이 조금은 깨끗해지고 평온해지기만을 바랄 뿐이야. "
test2 = "너처럼 웃어 주는 나 눈을 떴을 때 있던 네 가 이젠 눈을 감아야지"
x_list = tokenizer.texts_to_sequences(removepos(tokenize_sentense(test)))
x_list2 = tokenizer.texts_to_sequences(removepos(tokenize_sentense(test2)))
print(x_list)
print(x_list2)
xx_list = []
xx_list.append(x_list)
xx_list.append(x_list2)
# num_list, w2n_dic, n2w_dic= word2num(tokenize_sentense(test))
# # print(num_list)
# x_list = sequence.pad_sequences(num_list, maxlen =50)
# print(x_list)
y_prob = new_model.predict(x_list,verbose =0)
print(type(y_prob))
predicted = y_prob.argmax(axis=-1)
print(predicted)

lyric_emotion = ['슬픔', '부정', '분노', '무관심']
print(lyric_emotion[y_prob.sum(axis=0).argmax()])
