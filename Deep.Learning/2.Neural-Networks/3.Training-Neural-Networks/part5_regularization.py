import numpy as np

data = np.array([[1,1],[-1, -1]])
w1 = np.array([1,1])
w2 = np.array([10, 10])

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))

print("w1:",sigmoid(np.dot(data, w1)))
print("w2:",sigmoid(np.dot(data, w2)))
