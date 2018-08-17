import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []
for line in open('data_poly.csv'):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x*x])
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X[:, 1], Y)
# plt.savefig('poly.png')
# from PIL import Image
# img = Image.open('poly.png')
# img.show()

w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
Yhat = np.dot(X, w)

plt.clf()
plt.scatter(X[:, 1], Yhat)
plt.savefig('poly.png')
from PIL import Image
img = Image.open('poly.png')
img.show()
