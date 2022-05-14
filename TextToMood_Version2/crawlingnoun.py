#-*-Encoding:UTF-8 -*-#
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import konlpy
import nltk
import pickle
import requests
import urllib.request as req
import re
from konlpy.tag import Kkma
kkma = Kkma()
url = "https://blog.daum.net/9855/79"
res = req.urlopen(url).read()
html = urlopen(url).read()
from tensorflow.keras.preprocessing.text import Tokenizer
with open("TokenafterSentence.pickle","rb") as f:
    list_ex = pickle.load(f)
tokenizer = Tokenizer(19845)
tokenizer.fit_on_texts(list_ex)
import json
import numpy as np
address = 'http://localhost:8501/v1/models/LSTM:predict'
bsObject = BeautifulSoup(html, "html.parser") 
# print(bsObject) # 웹 문서 전체가 출력
# print(bsObject.get_text())
onlytext = bsObject.get_text()
# print(onlytext)
# print(type(onlytext))
# onlytext=onlytext.replace("\n","")
token = kkma.sentences(onlytext)
# print(token)
strlist = []
topthree = [0 for i in range(13)]
for i in token:
    # print(i)

    strlist.append(i)
    x_list = tokenizer.texts_to_sequences(strlist)
    strlist.clear()
    # print(x_list)
    if len(x_list[0]) == 0:
        continue
    data = json.dumps({'instances':x_list})
    result = requests.post(address, data=data)
    # print(result)
    predictions = json.loads(str(result.content, 'utf-8'))['predictions']
    lyric_emotion = ['성적', '기쁨', '두려움', '환상','반항','불안','승리','재미','아름다움','이별','짜증','편안','활력']
# print(predictions)
    for prediction in predictions:
        print(lyric_emotion[np.argmax(prediction)])
        topthree[np.argmax(prediction)]+=1
print(topthree)
sortlist=sorted(topthree)
print(sortlist)
print(topthree.index(sortlist[-1])+1)

# print(type(words[0]))

# grammar = """
# NP: {<N.*>*<Suffix>?}   # Noun phrase
# VP: {<V.*>*}            # Verb phrase
# AP: {<A.*>*}            # Adjective phrase
# """
# parser = nltk.RegexpParser(grammar)
# chunks = parser.parse(words)
# print("# Print whole tree")
# print(chunks.pprint())
# noun = []
# print("\n# Print noun phrases only")
# for subtree in chunks.subtrees():
#     if subtree.label()=='NP':
#         print(' '.join((e[0] for e in list(subtree))))
#         print(subtree.pprint())
#         noun.append(subtree)

# # Display the chunk tree
# chunks.draw()
# print(noun)