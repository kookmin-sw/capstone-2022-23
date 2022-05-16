
#2클롤링한 데이터를 문장 단위로 분리합니다. 
import copy
from konlpy.tag import Kkma
kkma = Kkma()
import pickle
import os
i=0
sentence =[]
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/관능'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/관능", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/기쁨'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/기쁨", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/두려움'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/두려움", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/몽환'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/몽환", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/반항'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/반항", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/불안'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/불안", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/승리'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/승리", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/신남'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/신남", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/아름다움'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/아름다움", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/이별'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/이별", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/짜증'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/짜증", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/평안'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/평안", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
       for index in range(len(token)):
           sentence.append(token[index])
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/활력'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/MusicdeciderEmotions/활력", filename), 'r') as f:
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

