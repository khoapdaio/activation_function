from scipy import special
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Sigmoid Function
# 1 numer
def sigmoidFunction(x):
    return 1 / (1 + np.exp(-x))


# 2 Array
def sigmoidFunctionArr(x):
    return 1 / (1 + np.exp(-(np.array(x))))


def tanhFunction(x):
    return np.tanh(x)


def tanhFunctionArr(x):
    return np.tanh(np.array(x))


print(sigmoidFunction(1))
print(sigmoidFunctionArr([-3, -2, -1, 1, 2, 3]))
print(tanhFunction(1))
print(tanhFunctionArr([1, 2, 4, 5, -2, 45, 24. - 234]))
