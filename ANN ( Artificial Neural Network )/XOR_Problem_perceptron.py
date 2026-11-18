
# Importing Python library
import numpy as np

# Define Unit Step Function
def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

# Design Perceptron Model
def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y

def XOR_logicFunction(x):

    w1 = np.array([1, -1])
    b1 = -0.5
    h1 = perceptronModel(x, w1, b1)

    w2 = np.array([-1, 1])
    b2 = -0.5
    h2 = perceptronModel(x, w2, b2)

    w3 = np.array([1, 1])
    b3 = -0.5

    # Calculate final XOR output
    hidden_output = np.array([h1, h2])
    y = perceptronModel(hidden_output, w3, b3)
    return y

# Testing the XOR Model
test1 = np.array([0, 0])
test2 = np.array([0, 1])
test3 = np.array([1, 0])
test4 = np.array([1, 1])

print("XOR({}, {}) = {}".format(0, 0, XOR_logicFunction(test1)))
print("XOR({}, {}) = {}".format(0, 1, XOR_logicFunction(test2)))
print("XOR({}, {}) = {}".format(1, 0, XOR_logicFunction(test3)))
print("XOR({}, {}) = {}".format(1, 1, XOR_logicFunction(test4)))
