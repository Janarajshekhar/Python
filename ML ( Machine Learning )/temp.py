import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#Step1: Create sample datasets

X,y=make_blobs(n_samples=300,
               centers=4,
               cluster_std=0.60,
               random_state=42
               )
#step2: Apply K-Means clustering

Kmeans=KMeans(
    n_clusters=4,
    random_state=42
    )
Kmeans.fit(X)
#Predicted cluster labels
labels=Kmeans.predict(X)

#Cluster centers

centroids=Kmeans.cluster_centers_
print(centroids)

#Step:3 Visualize clusters

plt.figure(figsize=(8,6))

#plot data points

plt.scatter(
    X[:,0],
    X[:,1],
    c=labels,
    cmap='viridis',
    s=50
    )   

#Plot centroids 

plt.scatter(
    centroids[:,0],
    centroids[:,1],
    c='red',
    marker='X',
    s=200,
    label='Centroids'
    )