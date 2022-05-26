import numpy as np
from math import*
import collections
import os
from PIL import Image
import pickle

def manhattan_distance(x, y): #manhattan distance
    return sum(abs(a-b) for a,b in zip(x,y))

#이미지별 색상 조합
di = dict()

#16가지 색상
psycolors = [[255,0,0], [255,165,0], [255,255,0], [0,128,0], [0,0,255], [75,0,130], [128,0,128], [64,224,208], [255,192,203], [255,0,255], [165,42,42], [128,128,128], [192,192,192], [255,215,0], [255,255,255], [0,0,0]]

dir = "D:/capstone-2022-23/img/emotion6/anger/"
for i in os.listdir(dir):
    path = dir + i
    print(path)

    src = Image.open(path)
    src = src.convert("RGB")
    src = np.array(src)
    print(src)

    data = src.reshape(-1, 3).astype(np.float32)

    counts = collections.Counter(map(tuple, data))

    combi = [counts.most_common(2)[0][0], counts.most_common(2)[1][0]]
    print(combi)

    for i in range(2):
        min = 999999
        for j in range(len(psycolors)):
            md = manhattan_distance(combi[i], psycolors[j])
            if md < min:
                min = md
                temp = psycolors[j]
        combi[i] = tuple(temp)

    combi = tuple(combi)
    print(combi)

    if combi in di:
        di[combi] += 1
    else:
        di[combi] = 1

    print(di)

with open('angry_dict.pkl','wb') as f:
    pickle.dump(di,f)