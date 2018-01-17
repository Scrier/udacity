import numpy as np


def calculate(x1, x2):
    return 1 / (1 + np.exp(-(4 * x1 + 5 * x2 - 9)))


print("calculate(1, 1) = ",calculate(1, 1),"=>",0.5 == calculate(1, 1))
print("calculate(2, 4) = ",calculate(2, 4),"=>",0.5 == calculate(2, 4))
print("calculate(5, -5) = ",calculate(5, -5),"=>",0.5 == calculate(5, -5))
print("calculate(-4, 5) = ",calculate(-4, 5),"=>",0.5 == calculate(-4, 5))
