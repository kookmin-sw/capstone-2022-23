#7. 만들어진 데이터셋으로 LSTM 모델을 위한 임베딩과 데이터터 결과를 원핫벡터로 바꾸는 과정을 진행하고 만들어진 모델을 저장합니다.
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
with open("TokenafterSentence.pickle","rb") as f:
    list_ex = pickle.load(f)
df = pd.read_csv("data_label.csv")
y_train = np.array(df['label'].to_list())
f.close()   
def tokenize_sentense(text): #토큰화를 진행합니다.
    kkma = Kkma()
    return kkma.pos(text)


def word2num(list_2d):
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


def divide_data(x, y, train_prop = 0.8):
    x = np.array(x)
    y = np.array(y)
    tmp = np.random.permutation(np.arange(len(x)))
    x_tr = x[tmp][:round(train_prop * len(x))]
    y_tr = y[tmp][:round(train_prop*len(x))]
    x_te = x[tmp][-(len(x)-round(train_prop*len(x))):]
    y_te = y[tmp][-(len(x)-round(train_prop * len(x))):]
    return x_tr, x_te, y_tr, y_te


num_list, w2n_dic, n2w_dic = word2num(list_ex)
x_tr, x_te, y_tr, y_te = divide_data(num_list, y_train)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(list_ex)
print(x_tr)
#num_words = 100 oov_token="<OOV>"
x_tr =sequence.pad_sequences(x_tr, maxlen =50)
print(len(x_tr[0]))
x_te = sequence.pad_sequences(x_te, maxlen =50)
y_tr = np_utils.to_categorical(y_tr,13)
print(y_tr)
y_te = np_utils.to_categorical(y_te,13) 
# print(word2num(list_ex))


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
words_num = 19845
# x_tr,x_te,y_tr,y_te
# words_num은 총 단어의 종류. +1을 해준 이유는 단어 수가 적은 글의 경우 빈 칸에 0이 있기 때문에.
model = Sequential()
model.add(Embedding(words_num+1, len(x_tr[0])))  # 사용된 단어 수 & input 하나 당 size
model.add(LSTM(len(x_tr[0])))

model.add(Dense(len(y_tr[0]), activation='softmax'))  # 카테고리 수

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# x_tr=np.asarray(x_tr).astype(np.float32)
# y_tr=np.asarray(y_tr).astype(np.float32)
history = model.fit(x_tr, y_tr, batch_size=100, epochs=20, validation_data=(x_te,y_te))
model.save('musicdecider')
tf.saved_model.save(model, 'LSTMTest/1')