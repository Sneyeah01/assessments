# -*- coding: utf-8 -*-
"""LVADSUSR120-SNEHAO-LAB1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IrPxcFYlqJ9NOeQthDotytudRiUcxI82
"""

import pandas as pd
data = pd.read_csv('/content/winequality-red.csv')
data.head()

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

print(data.isnull().sum())
imputer = SimpleImputer(strategy='mean')
data[['fixed acidity', 'residual sugar', 'pH' , 'volatile acidity' , 'citric acid' , 'sulphates','chlorides','free sulfur dioxide' ]] = imputer.fit_transform(data[['fixed acidity', 'residual sugar', 'pH', 'volatile acidity' , 'citric acid' , 'sulphates','chlorides','free sulfur dioxide']])

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
outliers = (data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))
data[outliers] = np.where(data[outliers] < (Q1 - 1.5 * IQR), Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)

data['quality'] = data['quality'].apply(lambda x: 'bad' if x <= 6 and x>=3 else 'good')


label_encoder = LabelEncoder()
data['quality'] = label_encoder.fit_transform(data['quality'])

features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
            'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
target = ['quality']

X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k_values = [3, 5, 7, 9]
for i in k_values:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train_scaled, y_train)
    y_pred = knn.predict(X_test_scaled)

#to predict the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    print(f'when knn is K={i}:')
    print(f' The Accuracy: {accuracy:.2f}, \n The Precision: {precision:.2f},\n The Recall: {recall:.2f}')

