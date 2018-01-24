import numpy as np
import string
import random

def random_string(length, seq='abcdefghijklmnopqrstuvwxyz,. '):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


f = open('76-0.txt')
data1 = f.read()
f.close()
data2=[data1[i:i+3200] for i in range(0, len(data1), 3200)]
print(len(data2))


