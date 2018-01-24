import numpy as np
import string
import random

def random_string(length, seq='abcdefghijklmnopqrstuvwxyz,. '):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


def gedata():
    f = open('76-0.txt')
    data1 = f.read()
    f.close()
    data2=[data1[i:i+3200] for i in range(0, len(data1), 3200)]
    aw=[]
    wl=[]
    bookdata=[]
    for x in range(100):
        for i in data2[x]:
            aw.append(ord(i))
        bookdata.append(aw)
        aw=[]

    for i in range(100):
        for w in random_string(3200):
            wl.append(ord(w))
        bookdata.append(wl)
        wl=[]

    return bookdata

train_x=np.array(gedata())
train_y=np.zeros(len(gedata()))
for j in range(100):
    train_y[j]=1
for i in range(200):
    print(len(train_x[i]))



