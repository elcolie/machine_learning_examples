import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
# plt.savefig('tmp.png')
# img = Image.open('tmp.png')
# img.show()

denominator = -X.mean() * X.sum() + X.dot(X)
a = (X.dot(Y) - X.mean() * Y.sum()) / denominator
b = (-X.mean() * X.dot(Y) + X.dot(X) * Y.mean()) / denominator
print(a)
print(b)

Yhat = a*X + b
plt.plot(X, Yhat, color='red')
plt.savefig('fit.png')
img = Image.open('fit.png')
img.show()

d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("the r-squared is:", r2)


