import tensorflow as tf
from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Conv2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications.densenet import DenseNet169
import numpy as np
import os
from PIL import Image

# 카테고리 지정하기
categories = ["anger","fear","joy","love","sadness","surprise"]
nb_classes = len(categories)
# 이미지 크기 지정하기
image_w = 64
image_h = 64
# 데이터 열기 
X_train, X_test, y_train, y_test = np.load("./7obj.npy", allow_pickle=True)
# 데이터 정규화하기(0~1사이로)
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

denseNet169 = DenseNet169(weights="imagenet", include_top=False, input_shape=(64, 64, 3))

# 모델 구조 정의 
model = Sequential()
model.add(denseNet169)
# 전결합층
model.add(Flatten())    # 벡터형태로 reshape

model.add(Dense(nb_classes))
model.add(Activation('softmax'))
# 모델 구축하기
model.compile(loss='categorical_crossentropy',   # 최적화 함수 지정
    optimizer='adam',
    metrics=['accuracy'])
# 모델 확인
#print(model.summary())

model.fit(X_train, y_train, batch_size=32, epochs=50)

model.evaluate(X_test, y_test)

tf.saved_model.save(model, 'IMGCLASS/1')