

#2클롤링한 데이터를 문장 단위로 분리합니다. 
import copy
from konlpy.tag import Kkma
kkma = Kkma()
import pickle
import os
i=0
sentence =[]
lyric_emotion = ['관능', '기쁨', '두려움', '몽환','반항','불안','승리','신남','아름다움','이별','짜증','편안','활력']
for i in lyric_emotion:
   for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/'+i):
      with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/"+i, filename), 'r') as f:
         text = f.read()
      #    print(text)
         print('\n ' + str(i))
         i = i+1
         token = kkma.sentences(text)
         print(token)
         
         for index in range(len(token)):
            sentence.append(token[index])

with open('list3.pickle', 'wb') as f:
    pickle.dump(sentence, f, pickle.HIGHEST_PROTOCOL)

f.close()


