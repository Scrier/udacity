import numpy as np


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    sum = 0
    for y, p in zip(Y, P):
        if y == 1:
            sum += -np.log(p)
        elif y == 0:
            sum += -np.log(1 - p)
    return sum


def with_print(Y, P):
    for i in range(len(Y)):
        print(Y[i], P[i])
    return cross_entropy(Y, P)


print(cross_entropy([1, 1, 0], [0.8, 0.7, 0.1]))
print(cross_entropy([1, 1, 0, 0, 1], [0.6, 0.8, 0.2, 0.4, 0.9]))
