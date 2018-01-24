import string
import random

def random_string(length, seq='abcdefghijklmnopqrstuvwxyz,. '):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])

print(random_string(3200))
