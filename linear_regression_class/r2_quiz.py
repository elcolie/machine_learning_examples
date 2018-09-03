# Use `systolic.py` as a starting point
# The data (X1, X2, X3) are for each patient.
# X1 = systolic blood pressure
# X2 = age in years
# X3 = weight in pounds

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('mlr02.xls')
X = df.values

# Age VS Pressure
plt.scatter(X[:,1], X[:,0])
# plt.show()
# Linear

# Weight VS Pressure
plt.scatter(X[:, 2], X[:, 0])
# plt.show()
# Linear

df['ones'] = 1  # Add bias term
df['noises'] = np.random.normal(0, 1, 11)
Y = df['X1']
X = df[['X2', 'X3', 'ones']]  # multiple dimension
X_noise = df[['X2', 'X3', 'ones', 'noises']]  # multiple dimension

def get_r2(X, Y):
    w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
    Yhat = X.dot(w)

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1)/d2.dot(d2)
    return r2

orig = get_r2(X, Y)
noise = get_r2(X_noise, Y)
print(f"r2 for orig: {orig}")
print(f"r2 for noise: {noise}")
print(f"gain: {(orig - noise)*100}")