# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Input data
data = {
    'Math': [78,85,96,80,86],
    'Science': [88,90,94,82,89],
    'English': [72,75,78,70,74]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute Pearson correlation between specific columns
correlation = df['Math'].corr(df['Science'])

# Display correlation value
print(f"Pearson Correlation between Hours Studied and Test Scores: {correlation:.4f}")

# Plot Heatmap
plt.figure(figsize=(8,6))

corr_matrix = df.corr()

sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')

plt.title("Pearson Correlation Heatmap")
plt.show()