import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

#1. Dataset:Hours studied (x) vs Pass/Fail (y)

x=np.array([0.5,0.75,1.0,1.25,1.5,1.75,1.75,2.0,2.25,2.5,2.75,3.0,3.25,3.5,4.0,4.25,4.5,4.75,5.0,5.5]).reshape(-1,1)
y=np.array([0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1])

#2. Train model
model=LogisticRegression()
model.fit(x,y)
y_pred=model.predict(x)

#3. Visualization

plt.figure(figsize=(12,5))

#Plot 1: Logistic Regression sigmoid curve
plt.subplot(1,2,1)
x_range=np.linspace(0,6,100).reshape(-1,1)
y_prob=model.predict_proba(x_range)[:,1]
plt.scatter(x,y,color='red',label='Actual Data')
plt.plot(x_range,y_prob,color='blue',label='Probablity Curve')
plt.axhline(0.5,color='black',linestyle='--') #Decision Threshold
plt.title("Study hours vs Pass Probablity")
plt.xlabel('Hours Studied')
plt.ylabel('Pass Probablity')
plt.legend()

#2. Plot 2: Confusion matrix Heatmap
plt.subplot(1,2,2)
cm=confusion_matrix(y,y_pred)
sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',xticklabels=['Fail','Pass'],yticklabels=['Fail','Pass'])
plt.title('Confusion Matrix')
plt.xlabel("Predicted Label")
plt.ylabel("True Label")

plt.tight_layout()
plt.show() 

#4. Print Detailed Metrics

print(classification_report(y,y_pred))

accuracy=accuracy_score(y,y_pred)
precision=precision_score(y,y_pred)
recall=recall_score(y,y_pred)
f1=f1_score(y,y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 score: {f1:.2f}")