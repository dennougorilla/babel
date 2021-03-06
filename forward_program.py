import numpy as np
import string
import random

def random_string(length, seq='abcdefghijklmnopqrstuvwxyz,. ;:[]()+-$%^&#@*!?/'""'|{}`~_=<>'):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])

def activation(x):
    return 1/(1+np.exp(-x))

def forward(x):
    return w2 @ activation(w1 @ x + b1) + b2

def soft(x):
    if x>=0.8:
        return 1
    else:
        return 0

#forward
w1=np.load('w1pro.npy')
w2=np.load('w2pro.npy')
b1=np.load('b1pro.npy')
b2=np.load('b2pro.npy')

for i in range(100000):
    tmp=random_string(3200)
    wdata=[]
    for w in tmp:
        wdata.append(ord(w))
    y=forward(wdata)
    print(y)
    if y>=0.9:
        f = open('true_book_pro.txt','w')
        f.write('\n')
        f.write(str(y))
        f.write('\n')
        f.write(tmp)
        f.write('\n')
        f.close()
        break


