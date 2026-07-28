import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#1. Dataset : Feature (x,y) and classes (0 or 1)
data = list(zip([4,5,10,4,3,11,14,8,10], [21,19,24,17,16,25,24,22,21]))
classes = [0,0,1,0,0,1,1,0,1]

#2. instantiate and fit the KNN model(k=3)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(data,classes) #stores training data

#3. Predict new point
new_point = [[8,21]]
prediction = knn.predict(new_point)

print(f"Pediction : {prediction[0]}")

#4. Visualize
plt.scatter([p[0] for p in data], [p[1] for p in data], c= classes)
plt.scatter(new_point[0][0], new_point[0][1], c = 'red', marker='+')
plt.show()