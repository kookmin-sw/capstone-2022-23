from gensim.models import KeyedVectors 
from gensim.models import Word2Vec as wv

    # hello.txt 파일을 쓰기 모드(w)로 열기
import pickle   
        

loaded_model = KeyedVectors.load_word2vec_format('/home/wjdxodnjs/MusicDecider/word2vec/word2vec' ) # 모델 로드 
# print(loaded_model['슬픔'])
# print(loaded_model.vectors.shape) 
# print(loaded_model.most_similar("", topn=5)) 
# print(loaded_model.most_similar("남대문", topn=5)) 
# print(loaded_model.similarity("헐크", '아이언맨')) 
# print(loaded_model.most_similar(positive=['어벤져스', '아이언맨'], negative=['스파이더맨'], topn=1))
lyric_emotion = ['슬픔', '부정', '분노', '무관심']
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