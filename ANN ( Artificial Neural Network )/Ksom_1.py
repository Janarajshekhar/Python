import numpy as np

X = np.array([
    [1,0,1,0], 
    [1,0,0,0], 
    [1,1,1,1], 
    [0,1,1,0]
], float)

W = np.array([
    [0.3,0.5,0.7,0.2], 
    [0.6,0.5,0.4,0.2]
], float)

alpha = 0.6
max_iterations = 1000

for epoch in range(1, max_iterations + 1):
    old_W = W.copy()

    print("Epoch:", epoch)
    for i, x in enumerate(X):
        d = np.sqrt(np.sum((W - x)**2, axis=1))
        winner = np.argmin(d)
        print(f"Input {X[i]} -- Winner: W{winner+1}")
        W[winner] += alpha * (x - W[winner])

    print("Weights after iteration", epoch)
    print("W1:", W[0], "\nW2:", W[1] ,"\n")

    if np.array_equal(np.round(W, 4), np.round(old_W, 4)):
        print("Convergence Reached!")
        break

print("\nFinal Weights:\n", np.round(W, 4))
print("Total Iterations:", epoch)
