import numpy as np

X = np.array([[1,1], [1,-1], [-1,1], [-1,-1]])
t = np.array([1,-1,-1,-1])

w1, w2, b, alpha, LSE = 0.1, 0.1, 0.1, 0.1, 2
i = 0

while True:
    i += 1
    E = 0

    for (x1, x2), target in zip(X, t):
        y = w1*x1 + w2*x2 + b
        e = target - y
        E += e**2
        w1 += alpha*e*x1
        w2 += alpha*e*x2
        b += alpha*e

    print(f"\nIteration {i} :")
    print(f"w1 = {w1:.4f}, w2 = {w2:.4f}, b = {b:.4f}")
    print(f"Total Squared Error = {E:.4f}")
    

    if E <= LSE:
        print("\nTraining stopped: Error condition satisfied.")
        break

print("\nFinal AND Gate Output:")
for x1, x2 in X:
    y = w1*x1 + w2*x2 + b
    print(f"{x1:2d} {x2:2d} -> y={y:.4f}, output={1 if y>=0 else -1}")