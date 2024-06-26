# -*- coding: utf-8 -*-
"""LVADSUSR120-Snehao-lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wXkNDy5PnEWNoe3Aunaw7jCqYWPtHfVU
"""

import pandas as pd
df = pd.read_csv('/content/expenses.csv')
df.head()


import matplotlib.pyplot as plt
import seaborn as sns

duplicate_vals = df[df.duplicated()]
print("\nDuplicate rows:")
print(duplicate_vals)
df.drop_duplicates(inplace=True)


print(df.isnull().sum())

print("Data has the following features:")
print(df.describe())

df.hist(figsize=(8, 8))
plt.tight_layout()
plt.show()

df.boxplot(figsize=(8, 6))
plt.tight_layout()
plt.show()

correlation= df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Chart')
plt.show()


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df["sex"] = label_encoder.fit_transform(df["sex"])
df["smoker"] = label_encoder.fit_transform(df["smoker"])
df["region"] = label_encoder.fit_transform(df["region"])

print(df.head())


from sklearn.preprocessing import StandardScaler
numericals = ['age', 'bmi','charges']
for feature in numericals:
    lower_bound = df[feature].quantile(0.05)
    upper_bound = df[feature].quantile(0.95)
    df[feature] = df[feature].clip(lower=lower_bound, upper=upper_bound)

#removing these columns as it has less correlation
df = df.drop('sex',axis=1)
df = df.drop('children',axis=1)
df = df.drop('region',axis=1)

X = df.drop(columns=['charges'])
y = df['charges']

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
scaled_data = pd.DataFrame(X_scaled, columns=X.columns)

scaled_data['Target'] = y

df.head()


from sklearn.model_selection import train_test_split

X = df[['age','bmi','smoker']]
y = df['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)


from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

accuracy = model.score(X_test, y_test)

Meansqaurederror = mean_squared_error(y_test, y_pred)

R_squared = r2_score(y_test, y_pred)

RMSE = sqrt(Meansqaurederror)

print("Accuracy:", accuracy)
print("MSE:", Meansqaurederror)
print("R-squared:", R_squared)
print("RMSE:", RMSE)