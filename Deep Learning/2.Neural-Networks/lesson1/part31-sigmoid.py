import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def calculate(w1, w2, bias):
    print("calculate(",w1,",",w2,",",bias,")")
    return sigmoid(w1*0.4 + w2 * 0.6 + bias)

print(calculate(2,6,-2))
print(calculate(3,5,-2.2))
print(calculate(5,4,-3))