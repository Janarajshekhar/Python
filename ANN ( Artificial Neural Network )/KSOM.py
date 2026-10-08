import numpy as np

X = np.array([
    [1, 0, 1, 0],    # X1
    [1, 0, 0, 0],    # X2
    [1, 1, 1, 1],    # X3
    [0, 1, 1, 0]     # X4
], dtype=float)

W_initial = np.array([
    [0.3, 0.5, 0.7, 0.2],    # W1
    [0.6, 0.5, 0.4, 0.2]     # W2
], dtype=float)

alpha = 0.6
max_iterations = 1000


def ksom(X, W_initial, alpha):

    W = W_initial.copy()

    # print("\n==============================================")
    print("        KSOM TRAINING STARTED")
    print("==============================================")
    print("\nLearning Parameter (alpha) =", alpha)

    for iteration in range(1, max_iterations + 1):

        old_W = W.copy()      # weights before this epoch

        print("\n")
        # print("==============================================")
        print("ITERATION / EPOCH:", iteration)
        print("==============================================")

        for i, x in enumerate(X):

            print("\nInput X{} = {}".format(i + 1, x.astype(int)))

            distance = np.sqrt(np.sum((W - x) ** 2, axis=1))

            print("Distance from W1 =", round(distance[0], 6))
            print("Distance from W2 =", round(distance[1], 6))

            winner = np.argmin(distance)
            print("Winner = W{}".format(winner + 1))

            W[winner] = W[winner] + alpha * (x - W[winner])

            print("Updated W{} = {}".format(winner + 1, np.round(W[winner], 6)))

        print("\n----------------------------------------------")
        print("Weights after iteration", iteration)
        print("----------------------------------------------")
        print("W1 =", np.round(W[0], 6))
        print("W2 =", np.round(W[1], 6))

        # Stop when old weights and new weights are the same (compared to 6 decimals)
        if np.array_equal(np.round(W, 6), np.round(old_W, 6)):

            # print("\n==============================================")
            print("CONVERGENCE REACHED")
            print("==============================================")
            print("Old weights and new weights are the same")
            print("\nTraining stopped at iteration:", iteration)
            break

    return W, iteration


final_W, total_iterations = ksom(X, W_initial, alpha)

# print("\n\n==============================================")
print("              FINAL RESULT")
print("==============================================")
print("\nLearning Parameter =", alpha)
print("\nFinal Weight W1:")
print(np.round(final_W[0], 6))
print("\nFinal Weight W2:")
print(np.round(final_W[1], 6))
print("\nTotal Iterations / Epochs Required:", total_iterations)
# print("==============================================")