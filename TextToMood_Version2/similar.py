#5.word2vec 모델을 가져와 분류하고 싶은 단어들로 유사도를 찾아 감정사전을 구축합니다.
from gensim.models import KeyedVectors 
from gensim.models import Word2Vec as wv
import pickle   
        

loaded_model = KeyedVectors.load_word2vec_format('/home/wjdxodnjs/MusicDecider/word2vec/word2vec' ) # 모델 로드 
lyric_emotion = ['성적', '기쁨', '두려움', '환상','반항','불안','승리','재미','아름다움','이별','짜증','편안','활력']
emotion_list = []

for index in range(len(lyric_emotion)):
    with open(lyric_emotion[index]+'.txt', 'w') as file:
        emotion_one = []
        i = 0
        for word in loaded_model.most_similar(lyric_emotion[index],topn= 10000):
            i+=1
            # print(i)
            if(word[1] > 0.5):
                emotion_one.append(word)
                file.write(str(word))
        emotion_list.append(emotion_one)
    # print(lyric_emotion[index], emotion_list[index])
# print(loaded_model.most_similar(lyric_emotion[1], topn=None))

with open('emotion_list.pickle', 'wb') as f:
    pickle.dump(emotion_list, f, pickle.HIGHEST_PROTOCOL)

f.close()