#3문장으로 나눠진 가사들을 kkma 라이브러리를 통해 품사단위로 나눕니다.
import copy
from konlpy.tag import Kkma
import pickle
import os
kkma = Kkma()


i=0
sentence =[]
with open("list3.pickle","rb") as f:
    list_ex = pickle.load(f) #문장이 담긴 리스트
for i in range(len(list_ex)): 
    text=list_ex[i]
    print('\n ' + str(i))
    i = i+1
    token = kkma.pos(text) #pos로 token화가 이루어진 문장을 token에 담습니다.
    
    result = [] #token을 담을 리스트
    temp = []
    print(token)
    for index in range(len(token)):
        word,tag = token[index]
        if tag in 'SF' or tag in 'SP' or tag in 'SS' or tag in 'SE' or tag in 'SO' or tag in 'SW'  or tag in 'ON': #불용어 품사를 제거합니다.
            continue      
        else:
            result.append(word)  
    if result: 
        temp = copy.deepcopy(result) 
        sentence.append(temp)
        result.clear()
       



with open('TokenafterSentence.pickle', 'wb') as f:
    pickle.dump(sentence, f, pickle.HIGHEST_PROTOCOL)
f.close()
