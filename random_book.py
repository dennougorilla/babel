import string
import random


def random_string(length, seq='abcdefghijklmnopqrstuvwxyz,. '):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


wl=[]
bookdata=[]
print(random_string(3200))
for i in range(100):
    for w in random_string(3200):
        wl.append(ord(w))
    bookdata.append(wl)
    print(len(wl))
    wl=[]


print(len(bookdata))
