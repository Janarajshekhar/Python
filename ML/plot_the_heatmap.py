# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Input data
data = {
    'Hours_studied': [10, 8, 15, 18, 5, 20, 12, 14, 7, 11],
    'Test_scores': [85, 78, 92, 95, 60, 98, 88, 90, 72, 82],
    'Coffin_intake': [2, 1, 3, 4, 1, 5, 2, 3, 1, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute Pearson correlation between specific columns
correlation = df['Hours_studied'].corr(df['Test_scores'])

# Display correlation value
print(f"Pearson Correlation between Hours Studied and Test Scores: {correlation:.4f}")

# Plot Heatmap
plt.figure(figsize=(8,6))

corr_matrix = df.corr()

sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm',
            fmt='.2f')

plt.title("Pearson Correlation Heatmap")
plt.show()