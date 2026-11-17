# importing Python library
import numpy as np

# define Unit Step Function
def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

# design Perceptron Model
def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

# NOR Logic Function
# w1 = 1, w2 = 1, b = 0.5
def NOR_logicFunction(x):
    w = np.array([-1, -1])
    b = 0.5
    return perceptronModel(x, w, b)

# testing the Perceptron Model
test1 = np.array([0, 0])
test2 = np.array([0, 1])
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("NOR({}, {}) = {}".format(0, 0, NOR_logicFunction(test1)))
print("NOR({}, {}) = {}".format(0, 1, NOR_logicFunction(test2)))
print("NOR({}, {}) = {}".format(1, 0, NOR_logicFunction(test3)))
print("NOR({}, {}) = {}".format(1, 1, NOR_logicFunction(test4)))