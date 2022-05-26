#6. 토큰화된 단어들의 리스트인 list_ex와 word2vec으로 만든 단어유사도 emolist_ex를 사용하여 문장 단위로 점수를 계산합니다.
import pickle
import os
import pandas as pd
import numpy as np
with open("emotion_list.pickle","rb") as f:
    emolist_ex = pickle.load(f)
f.close()
with open("list3.pickle","rb") as f:
    list_ex = pickle.load(f)
f.close
print(len(emolist_ex[0]),len(emolist_ex[1]),len(emolist_ex[2]),len(emolist_ex[3]),len(emolist_ex[4]),len(emolist_ex[5]),len(emolist_ex[6]),len(emolist_ex[7]),len(emolist_ex[8]),len(emolist_ex[9]),len(emolist_ex[10]),len(emolist_ex[11]),len(emolist_ex[12])) #감정 사전에 들어있는 단어들의 개수 ( 유사도 0.5 이상 )
lyric_emotion = ['성적', '기쁨', '두려움', '환상','반항','불안','승리','재미','아름다움','이별','짜증','편안','활력']

data_dic = {lyric_emotion[0]: 0,
 lyric_emotion[1]:0,
lyric_emotion[2]:0,
lyric_emotion[3]:0,
lyric_emotion[4]:0,
lyric_emotion[5]:0,
lyric_emotion[6]:0,
lyric_emotion[7]:0,
lyric_emotion[8]:0,
lyric_emotion[9]:0,
lyric_emotion[10]:0,
lyric_emotion[11]:0,
lyric_emotion[12]:0} #각 감정마다 점수를 가진 dictionary를 생성합니다.

def whatIsBest(x):
    return data_dic[x]

result_list = []
temp = []
data_temp = pd.Series(temp) #series 객체로 데이터를 담습니다.
def pandadata(temp): 
    for k in range(len(lyric_emotion)):
        for i in emolist_ex[k]:
            for j in range(len(temp)):
                if i[0] == temp[j]:
                    # print(i[1])
                    data_dic[lyric_emotion[k]]= data_dic[lyric_emotion[k]]+i[1]
    best_emotion = max(data_dic.keys(), key = whatIsBest)
    result_list.append(best_emotion) #문장에서 값이 제일 높은 감정만 뽑아서 결과 리스트에 담습니다.
    data_dic[lyric_emotion[0]] = 0
    data_dic[lyric_emotion[1]] = 0
    data_dic[lyric_emotion[2]] = 0
    data_dic[lyric_emotion[3]] = 0
    data_dic[lyric_emotion[4]] = 0
    data_dic[lyric_emotion[5]] = 0
    data_dic[lyric_emotion[6]] = 0
    data_dic[lyric_emotion[7]] = 0
    data_dic[lyric_emotion[8]] = 0
    data_dic[lyric_emotion[9]] = 0
    data_dic[lyric_emotion[10]] = 0
    data_dic[lyric_emotion[11]] = 0
    data_dic[lyric_emotion[12]] = 0
    


lyric_emotion = ['성적', '기쁨', '두려움', '환상','반항','불안','승리','재미','아름다움','이별','짜증','편안','활력']

for i in range(len(list_ex)): #문장단위로 가져와 위에서 구현한 문장마다 감정을 부여하는 함수에 넣습니다.
    pandadata(list_ex[i])
temp =[]
data_temp = pd.Series(list_ex)
result_pd = pd.Series(result_list)
label_df = {"성적":0, "기쁨":1, "두려움":2, "환상":3, "반항":4,"불안":5,"승리":6,"재미":7,"아름다움":8,"이별":9,"짜증":10,"편안":11,"활력":12}

data_label = pd.concat([data_temp,result_pd],axis=1) 
data_label["label"] = data_label.iloc[:,1].map(label_df) #위에서 정한 항복으로 라벨링을 진행합니다.
print(type(data_label))
data_label = data_label.astype({'label': 'int'})
data_label.to_csv("data_label.csv") #해당 데이터를 csv로 저장합니다.
# print(data_label.head(200))


