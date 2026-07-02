import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

#step1 : create sample dataset
x,y = make_blobs(
    n_samples = 300,
    centers = 4,
    #clusters = 4,
    cluster_std=0.60,
    random_state = 42    
)

#step2 : Apply K-means clustring
kmeans = KMeans(
    n_clusters = 4,
    random_state = 42
)
kmeans.fit(x)

#predicted cluster labels
labels = kmeans.predict(x)

#cluster centers
centroides = kmeans.cluster_centers_
print(centroides)

#step3 : Visualize clusters
plt.figure(figsize=(8,6))

#plot data points
plt.scatter(
    x[:,0], 
    x[:,1], 
    c = labels,
    cmap = 'viridis',
    s = 50
)

#plot centroids
plt.scatter(
    centroides[:,0], 
    centroides[:,1],
    c = 'red',
    marker = 'X',
    s = 200,
    label = 'centroides'
)
