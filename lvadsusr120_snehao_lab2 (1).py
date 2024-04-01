# -*- coding: utf-8 -*-
"""LVADSUSR120-SNEHAO-lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PU0_a2kN0WYUxs-EKZhmHaSWVXou3x_J
"""

import pandas as pd
df=pd.read_csv('/content/Mall_Customers.csv')



import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df.fillna(df.mean(), inplace=True)


df['Age_Income_Ratio'] = df['Age'] / df['Annual Income (k$)']
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)', 'Age_Income_Ratio']])

inertia_values = []
silhouette_scores = []
kvals = range(4, 12)
for i in kvals:
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))

plt.plot(kvals, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Curve for Optimal k')
plt.xticks(kvals)
plt.show()

plt.plot(kvals, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k')
plt.xticks(kvals)
plt.show()

optimal_k = 5
k_means = KMeans(n_clusters=optimal_k, random_state=42)
k_means.fit(scaled_data)

cluster_labels = k_means.predict(scaled_data)

silhouette_avg = silhouette_score(scaled_data, cluster_labels)
print("silhouette score: ",silhouette_avg)


df['Cluster'] = kmeans.labels_
cluster_profiles = df.groupby('Cluster').mean()
print(cluster_profiles)

"""
 Product with appropriate price range can be promoted to their corresponding age group cluster and hence enhance the probability of a customer to spend on that product"""