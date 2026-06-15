from sklearn.model_selection import train_test_split

# Example dataset
X = list(range(100))      # Features
Y = list(range(100))      # Labels

# Step 1: Split data into Training (70%) and Testing (30%)
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.3, random_state=42)
# Step 2: Split Training data into Training (75% of 80%) and Validation (25% of 80%)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)
# Display dataset sizes
print(f"Train size: {len(X_train)}")
print(f"Validation size: {len(X_val)}")
print(f"Test size: {len(X_test)}")


# Step 1: Split data into Training (70%) and Testing (30%)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Step 2: Split Training data into Training (75% of 80%) and Validation (25% of 80%)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.25, random_state=42)
# Display dataset sizes
print(f"Train size: {len(X_train)}")
print(f"Validation size: {len(X_val)}")
print(f"Test size: {len(X_test)}")