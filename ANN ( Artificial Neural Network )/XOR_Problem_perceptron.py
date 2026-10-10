
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

# XOR Logic Function using a Multilayer Perceptron
def XOR_logicFunction(x):

    # Hidden layer: OR and NAND
    w_or = np.array([1, 1])
    b_or = -0.5

    w_nand = np.array([-1, -1])
    b_nand = 1.5

    # Output layer: AND
    w_and = np.array([1, 1])
    b_and = -1.5

    # Calculate hidden layer outputs
    h1 = perceptronModel(x, w_or, b_or)    # OR
    h2 = perceptronModel(x, w_nand, b_nand) # NAND

    # Calculate final XOR output
    hidden_output = np.array([h1, h2])
    y = perceptronModel(hidden_output, w_and, b_and)

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
