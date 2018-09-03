import numpy as np
import matplotlib

from sarit_process import get_binary_data

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

X, Y = get_binary_data()

D = X.shape[1]
W = np.random.randn(D)  # Weight on features. Thus D dimension
b = 0


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


def forward(X, W, b):
    return sigmoid(X.dot(W) + b)


P_Y_given_X = forward(X, W, b)
predictions = np.round(P_Y_given_X)


def classification_rate(Y, P):
    return np.mean(Y == P)


def main():
    print(f"Score: {classification_rate(Y, predictions)}")


if __name__ == '__main__':
    main()
