# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:06:12 2019

@author: amitabh.gunjan
"""

from time import time
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.externals import joblib

from dask.distributed import Client

client = Client()  # Connect to a Dask Cluster
data = fetch_olivetti_faces()
X = data.images.reshape((len(data.images), -1))
y = data.target
print(y)

mask = y < 5  # Limit to 5 classes
X = X[mask]
y = y[mask]
forest = ExtraTreesClassifier(n_estimators=1000,
                              max_features=128,
                              n_jobs=-1,
                              random_state=0)
# Build a forest and compute the pixel importances

t0 = time()
with joblib.parallel_backend('dask'):
    forest.fit(X, y)

print("done in %0.3fs" % (time() - t0))
importances = forest.feature_importances_
importances = importances.reshape(data.images[0].shape)

# Plot pixel importances
plt.matshow(importances, cmap=plt.cm.hot)
plt.title("Pixel importances with forests of trees")
plt.show()