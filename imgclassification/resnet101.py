from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Conv2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.applications.resnet import ResNet101
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

resNet101 = ResNet101(weights="imagenet", include_top=False, input_shape=(64, 64, 3))

# 모델 구조 정의 
model = Sequential()
model.add(resNet101)
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

# 학습 완료된 모델 저장
hdf5_file = "./resnet101-model.hdf5"
if os.path.exists(hdf5_file):
    # 기존에 학습된 모델 불러들이기
    model.load_weights(hdf5_file)
else:
    # 학습한 모델이 없으면 파일로 저장
    model.fit(X_train, y_train, batch_size=32, epochs=50)
    model.save_weights(hdf5_file)

score = model.evaluate(X_test, y_test)
print('loss=', score[0])        # loss
print('accuracy=', score[1])    # acc

test_image = './testimg_unknown.jpg'
# 이미지 resize
img = Image.open(test_image)
img = img.convert("RGB")
img = img.resize((64,64))
data = np.asarray(img)
X = np.array(data)
X = X.astype("float") / 256
X = X.reshape(-1, 64, 64,3)
# 예측
pred = model.predict(X)  
result = [np.argmax(value) for value in pred]   # 예측 값중 가장 높은 클래스 반환
print('New data category : ',categories[result[0]])