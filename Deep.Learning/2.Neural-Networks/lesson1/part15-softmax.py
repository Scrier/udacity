import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    divisor = sum(np.exp(i) for i in L)
    return list(np.exp(i)/divisor for i in L)

print(softmax([1,2,3,4,5]))
