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
    data2=[data1[i:i+32] for i in range(0, len(data1), 32)]
    aw=[]
    wl=[]
    bookdata=[]
    for x in range(1000):
        for i in data2[x]:
            aw.append(ord(i))
        bookdata.append(aw)
        aw=[]

    for i in range(1000):
        for w in random_string(32):
            wl.append(ord(w))
        bookdata.append(wl)
        wl=[]

    return bookdata


dim_in = 32
dim_out = 1            
hidden_count = 300   
learn_rate = 0.0005    
train_count = len(gedata())
train_x = np.asarray(gedata(),dtype=np.int32)
train_y = np.zeros(len(gedata()))
for i in range(1000):
    train_y[i]=1

w1 = np.random.rand(hidden_count, dim_in) - 0.5
w2 = np.random.rand(dim_out, hidden_count) - 0.5
b1 = np.random.rand(hidden_count) - 0.5
b2 = np.random.rand(dim_out) - 0.5

#w1=np.load('w1.npy')
#w2=np.load('w2.npy')
#b1=np.load('b1.npy')
#b2=np.load('b2.npy')

def activation(x):
    return 1/(1+np.exp(-x))

def activation_dash(x):
    return (1-activation(x))*activation(x)

def forward(x):
    return w2 @ activation(w1 @ x + b1) + b2

def backward(x, diff):
    global w1, w2, b1, b2
    v1 = (diff @ w2) * activation_dash(w1 @ x + b1)
    v2 = activation(w1 @ x + b1)

    w1 -= learn_rate * np.outer(v1, x)  # outerは直積
    b1 -= learn_rate * v1
    w2 -= learn_rate * np.outer(diff, v2)
    b2 -= learn_rate * diff
def soft(x):
    if x>=0.5:
        return 1
    else:
        return 0

idxes = np.arange(train_count)       
for epoc in range(10000):             
    np.random.shuffle(idxes)       
    error = 0                        
    for idx in idxes:
        y = forward(train_x[idx])    
        diff = y - train_y[idx]      
        if diff>1.0e+155:
            diff=np.array(1.0e+155)
        error += diff ** 2           
        backward(train_x[idx], diff) 
    print(error.sum())               
    np.save('w1.npy',w1)
    np.save('w2.npy',w2)
    np.save('b1.npy',b1)
    np.save('b2.npy',b2)

#forward

#np.load('w1.npy')
tmp=random_string(32)
wdata=[]
for w in tmp:
    wdata.append(ord(w))

y=forward(wdata)
print(y)



