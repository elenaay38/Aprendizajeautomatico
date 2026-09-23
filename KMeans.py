import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. Crear datos de ejemplo sintéticos (3 grupos)
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

# 2. Definir y entrenar el modelo K-Means
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# 3. Obtener resultados
etiquetas = kmeans.labels_
centroides = kmeans.cluster_centers_

# 4. Graficar los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=etiquetas, cmap='viridis', s=30, alpha=0.7)
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, marker='X', label='Centroides')
plt.title(f'K-Means con scikit-learn (K = {k})')
plt.legend()
plt.show()