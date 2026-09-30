import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay,classification_report,accuracy_score,precision_score,recall_score,f1_score

# Sample data (Actual labels and Predicted labels)
Y_true = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
Y_pred = [0, 1, 0, 0, 0, 1, 1, 1, 1, 0]

# Compute confusion matrix
cm = confusion_matrix(Y_true, Y_pred)

print("Confusion Matrix:\n", cm)

# Calculate performance metrics
print(f"Accuracy : {accuracy_score(Y_true, Y_pred):.2f}")
print(f"Precision: {precision_score(Y_true, Y_pred):.2f}")
print(f"Recall   : {recall_score(Y_true, Y_pred):.2f}")
print(f"F1 Score : {f1_score(Y_true, Y_pred):.2f}")

# Classification Report
print("\nClassification Report:\n")
print(classification_report(Y_true, Y_pred))

# Display Confusion Matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Negative", "Positive"]
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix Visualization")
plt.show()