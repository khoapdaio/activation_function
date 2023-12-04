from scipy import special
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# Sigmoid Function
# 1 numer
def sigmoidFunction(x):
    y = 1 / (1 + np.exp(-x))
    return y
# 2 Array
def sigmoidFunctionArr(x):
    y = []
    for temp in x:
        y.append(sigmoidFunction(temp))
    return y


print(sigmoidFunction(1))
print(sigmoidFunctionArr([1, 2, 4, 5, -2, 45, 24. - 234]))
