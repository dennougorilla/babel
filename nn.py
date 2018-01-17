import numpy as np

dim_in = 1
dim_out = 1            
hidden_count = 1024     
learn_rate = 0.005    

train_count = 64    
train_x = np.arange(-1, 1, 2 / train_count).reshape((train_count, dim_in))
train_y = np.array([2 * x ** 2 - 1 for x in train_x]).reshape((train_count, dim_out))

w1 = np.random.rand(hidden_count, dim_in) - 0.5
w2 = np.random.rand(dim_out, hidden_count) - 0.5
b1 = np.random.rand(hidden_count) - 0.5
b2 = np.random.rand(dim_out) - 0.5

def activation(x):
    return np.maximum(0, x)

def activation_dash(x):
    return (np.sign(x) + 1) / 2

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

idxes = np.arange(train_count)       
for epoc in range(1000):             
    np.random.shuffle(idxes)       
    error = 0                        
    for idx in idxes:
        y = forward(train_x[idx])    
        diff = y - train_y[idx]      
        error += diff ** 2           
        backward(train_x[idx], diff) 
    print(error.sum())               
