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
print(len(emolist_ex[0]),len(emolist_ex[1]),len(emolist_ex[2]),len(emolist_ex[3]))


lyric_emotion = ['슬픔', '부정', '분노', '무관심']
data_dic = {lyric_emotion[0]: 0, lyric_emotion[1]:0, lyric_emotion[2]:0,
lyric_emotion[3]:0}


# for k in range(len(lyric_emotion)):
#     for i in list_ex[k]:
#         for j in range(len(data_test)):
#             if i[0] == data_test[j]:
#                 print(i[1])
#                 data_dic[lyric_emotion[k]]= data_dic[lyric_emotion[k]]+i[1]
# print(data_dic)


def whatIsBest(x):
    return data_dic[x]

best_emotion = max(data_dic.keys(), key = whatIsBest)
print(best_emotion, data_dic[best_emotion])

result_list = []
temp = []
data_temp = pd.Series(temp)
def pandadata(temp): 
    

    
    for k in range(len(lyric_emotion)):
        for i in emolist_ex[k]:
            for j in range(len(temp)):
                if i[0] == temp[j]:
                    # print(i[1])
                    data_dic[lyric_emotion[k]]= data_dic[lyric_emotion[k]]+i[1]
    
    best_emotion = max(data_dic.keys(), key = whatIsBest)
    result_list.append(best_emotion)
    # label_df = {'슬픔':0,'부정':1,'무관심':2,'분노':3}
    # data_label["label"] = data_label.iloc[:,1].map(label_df)
    # best_emotion = max(data_dic.keys(), key = whatIsBest)
    
    # print(best_emotion, data_dic[best_emotion])
    data_dic[lyric_emotion[0]] = 0
    data_dic[lyric_emotion[1]] = 0
    data_dic[lyric_emotion[2]] = 0
    data_dic[lyric_emotion[3]] = 0

lyric_emotion = ['슬픔', '부정', '분노', '무관심']


# for index in range(len(lyric_emotion)):
#     list_ex[index]

for i in range(len(list_ex)):
    pandadata(list_ex[i])
temp =[]
data_temp = pd.Series(list_ex)
result_pd = pd.Series(result_list)
label_df = {"슬픔":0, "부정":1, "무관심":2, "분노":3}

data_label = pd.concat([data_temp,result_pd],axis=1)
data_label["label"] = data_label.iloc[:,1].map(label_df)
print(type(data_label))
data_label = data_label.astype({'label': 'int'})
data_label.to_csv("data_label.csv")
# print(data_label.head(200))


# y_train = data_label["label"].astype(int)
# print(y_train)
# # X_train = data_label[0]
# # print(X_train)
# np.unique(y_train)