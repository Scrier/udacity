import numpy as np


def calculate(ex1, ex2, ebias, ex, ey):
    print("x1:", ex1, ",x2:", ex2, "bias:", ebias, "x:", ex, "y:", ey)
    return ex * ex1 + ey * ex2 + ebias


x = 1
y = 1
x1 = 3
x2 = 4
bias = -10
iterations = -1  # we don't calculate the first time as that is the known output. Hence -1
factor = 0.1

while 0 >= calculate(x1, x2, bias, x, y):
    x1 = round(x1 + x * factor, 1)  # round the decimal point to 1 decimal.
    x2 = round(x2 + y * factor, 1)  # round the decimal point to 1 decimal.
    bias = round(bias + 1 * factor, 1)  # round the decimal point to 1 decimal.
    iterations = iterations + 1
    print(iterations)

print(x1, x2, bias, iterations)

print("step 9:", calculate(3.9, 4.9, -9.1, 1, 1))
print("step 10:", calculate(4.0, 5.0, -9.0, 1, 1))
