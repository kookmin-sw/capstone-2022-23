#4. 불용어를 제거한 토큰화된 단어들을 통해 word2vec 모델에 집어넣습니다. 
from gensim.models import Word2Vec 
from gensim.models.callbacks import CallbackAny2Vec 
from tqdm import tqdm
import pickle
import os
with open("TokenafterSentence.pickle","rb") as f: 
    list_ex = pickle.load(f)
f.close
print(len(list_ex)) #문장의 개수 확인
model_fname = '/home/wjdxodnjs/MusicDecider/word2vec/word2vec' 
class callback(CallbackAny2Vec): #callback 함수를 구현하여 epoch마다 손실 결과를 표현합니다.
     """Callback to print loss after each epoch.""" 


     def __init__(self):
        self.epoch = 0 
        self.loss_to_be_subed = 0 
     def on_epoch_end(self, model): 
        loss = model.get_latest_training_loss() 
        loss_now = loss - self.loss_to_be_subed 
        self.loss_to_be_subed = loss 
        print('Loss after epoch {}: {}'.format(self.epoch, loss_now)) 
        self.epoch += 1 

print("학습 중")  
#batch는 1000 window 는 5 차원은 150 sg = 0는 cbow를 의미합니다. 
model = Word2Vec(list_ex, vector_size=150, sg=0, compute_loss=True, epochs=10,min_count=1, callbacks=[callback()],batch_words=1000, window=5) 

model.wv.save_word2vec_format(model_fname)  #해당 모델을 저장합니다.
print('완료')

