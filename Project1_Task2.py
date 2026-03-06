'''
    Task 2:
    Design a recursive top‑down clustering algorithm with designated number of clusters.

    Required action with clustering algorithm

    Step 1 — Clustering : Apply your from‑scratch clustering algorithm to 10,000 time instances, each with 52 sensor measurements, and produce 4 clusters.
    Step 2 — Majority Class Count per Cluster : For each cluster, compute the count of the majority true class (based on your four RUL categories).
    Step 3 — Mapping Discussion : Briefly discuss how each cluster maps to a class (i.e., which class dominates each cluster and whether that alignment makes sense).
'''

import numpy as np
from collections import Counter

def divideAndConquerCluster(X, data_indices, k):
    if k == 1:
        return [data_indices]

    subset = X[data_indices]
    variances = np.var(subset, axis=0)
    split_dim = np.argmax(variances)
    values = subset[:, split_dim]
    median = np.median(values)

    left = []
    right = []

    for idx in data_indices:
        if X[idx, split_dim] <= median:
            left.append(idx)
        else:
            right.append(idx)

    k_left = k // 2
    k_right = k - k_left

    return (divideAndConquerCluster(X, left, k_left) + divideAndConquerCluster(X, right, k_right))

def runTask2(df, sensor_cols):
    X = df[sensor_cols].values

    labels = df["rul_category"].values

    indices = list(range(len(X)))

    clusters = divideAndConquerCluster(X, indices, 4)

    for i, cluster in enumerate(clusters):

        cluster_labels = [labels[idx] for idx in cluster]

        counts = Counter(cluster_labels)

        print("\nCluster", i)

        print("Cluster Size:", len(cluster))

        print("Majority Class:", counts.most_common(1)[0])