import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

L2 = []

for e in L:
    L2.append(e + e)

a = np.array([1, 2])
b = np.array([2, 1])

M = np.array([ [1,2], [3, 4]])

A = np.array([[1,2], [3,4]])
Ainv = np.linalg.inv(A)