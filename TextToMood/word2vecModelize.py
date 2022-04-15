from gensim.models import Word2Vec 
from gensim.models.callbacks import CallbackAny2Vec 
from tqdm import tqdm
import pickle
import os
with open("TokenafterSentence.pickle","rb") as f:
    list_ex = pickle.load(f)
f.close
print(len(list_ex))
# corpus_fname = '/home/wjdxodnjs/MusicDecider/1  2  3.txt' 
model_fname = '/home/wjdxodnjs/MusicDecider/word2vec/word2vec' 
class callback(CallbackAny2Vec):
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
print('corpus 생성') 
# corpus = [sent.strip().split(" ") for sent in tqdm(open(list_ex, 'r', encoding='utf-8').readlines())] 
print("학습 중") 
model = Word2Vec(list_ex, vector_size=150, sg=0, compute_loss=True, epochs=10,min_count=1, callbacks=[callback()],batch_words=1000, window=5) 
model.wv.save_word2vec_format(model_fname) 
print('완료')

