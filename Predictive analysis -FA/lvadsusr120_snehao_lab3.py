# -*- coding: utf-8 -*-
"""LVADSUSR120-SnehaO-lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JK4rJ4trMczOijJ8d6mQK4-3q-npGrS3
"""

import pandas as pd
df = pd.read_csv("/content/seeds.csv")
df.head()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
df.describe()
print(df.shape)
print(df.info())
print(df.describe())
df.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()
sns.pairplot(df, diag_kind='kde')
plt.show()
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation map')
plt.show()
inertia_values = []
silhouette_scores = []
k_values = range(2, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia_values.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(scaled_data, kmeans.labels_))
plt.plot(k_values, inertia_values, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow_Curve for Optimal k value ')
plt.xticks(k_values)
plt.show()

plt.plot(k_values, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Scores for Optimal k')
plt.xticks(k_values)
plt.show()
optimal_k = 7
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_data)
cluster_labels = kmeans.predict(scaled_data)
silhouette_avg = silhouette_score(scaled_data, cluster_labels)
print("Average silhouette score: ",silhouette_avg)
df['Cluster'] = kmeans.labels_
cluster_profiles = df.groupby('Cluster').mean()
print(cluster_profiles)

