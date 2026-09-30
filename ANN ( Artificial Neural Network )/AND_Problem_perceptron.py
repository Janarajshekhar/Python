import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        # Initialize weights to zero (+1 for the bias term)
        self.weights = np.zeros(input_size + 1)
        self.lr = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        # Heaviside Step Function: returns 1 if x >= 0, else 0
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        # Add bias input (1) to the features vector
        inputs_with_bias = np.insert(inputs, 0, 1)
        # Compute the dot product of inputs and weights
        linear_output = np.dot(inputs_with_bias, self.weights)
        return self.activation_function(linear_output)

    def fit(self, X, y):
        for epoch in range(self.epochs):
            for inputs, label in zip(X, y):
                prediction = self.predict(inputs)
                # Perceptron learning rule: weight update rule
                error = label - prediction
                if error != 0:
                    inputs_with_bias = np.insert(inputs, 0, 1)
                    self.weights += self.lr * error * inputs_with_bias

# --- Training Data for the AND Gate ---
# X = Input features (Truth table combinations)
# y = Target output labels
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 0, 0, 1])

# Initialize the Perceptron for 2 input features
perceptron = Perceptron(input_size=2, learning_rate=0.1, epochs=10)

# Train the model
perceptron.fit(X, y)

# --- Test the trained model ---
print("Trained Weights (including bias at index 0):", perceptron.weights)
print("\nTesting AND Gate Predictions:")
for inputs in X:
    print(f"Input: {inputs} -> Predicted Output: {perceptron.predict(inputs)}")
