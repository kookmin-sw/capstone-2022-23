
# import os
# currentPath = os.getcwd()

# print(currentPath)
import copy
from konlpy.tag import Kkma
kkma = Kkma()
sentence = "너무 그리워 부르고 또 부른다."
import pickle
import os
i=0
sentence =[]
for filename in os.listdir('/home/wjdxodnjs/MusicDecider/이별'):
   with open(os.path.join("/home/wjdxodnjs/MusicDecider/이별", filename), 'r') as f:
       text = f.read()
    #    print(text)
       print('\n ' + str(i))
       i = i+1
       token = kkma.sentences(text)
       print(token)
        
    #    stopword = []
    #    result = []
    #    temp = []
    #    print(token)
       for index in range(len(token)):
           sentence.append(token[index])
    #         word,tag = token[index]
    #         if tag in 'SF' or tag in 'SP' or tag in 'SS' or tag in 'SE' or tag in 'SO' or tag in 'SW'  or tag in 'ON':
    #             continue
    #         elif tag in 'EFN'or tag in 'EFQ' or tag in 'EFO' or tag in 'EFA' or tag in 'EFI' or tag in 'EFR':
    #             result.append(word)
    #             print(result)
    #             temp = copy.deepcopy(result)
    #             sentence.append(temp)
    #             result.clear()
    #         else:
    #             result.append(word)
    #    if result:
    #        temp = copy.deepcopy(result) 
    #        sentence.append(temp)
    #        result.clear()
    #    print(sentence)
# print(stopword)
# f = open('/home/wjdxodnjs/MusicDecider/1  2  3.txt', 'r')
# x= f.read()

# print(token[0],token[1],token[2])


with open('list3.pickle', 'wb') as f:
    pickle.dump(sentence, f, pickle.HIGHEST_PROTOCOL)

f.close()

# from gensim.models import Word2Vec as wv
# ###태깅한 데이터들을 담은 변수 :tagging_cut1_kkma

# model_kkma = wv(result, vector_size=100, workers=4, sg=1, compute_loss=True, epochs=5)


# lyric_emotion = [ '슬픔', '부정', '분노','무관심']
# emotion_list = [] 
# for index in range(len(lyric_emotion)):
#     emotion_one = [] #1개의 감정 단어가 담길 리스트
#     for word in model_kkma.wv.most_similar(lyric_emotion[index]):
#         print(word[0],word[1])
#         if(word[1] >= 0.5): # 튜플형식, 1번째 인덱스의 유사도와 비교
#             emotion_one.append(word)
#         emotion_list.append(emotion_one)
# print(emotion_list)