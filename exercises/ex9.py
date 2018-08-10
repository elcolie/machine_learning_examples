import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# I want self-contained in single file
from PIL import Image


def get_spiral(r, time, phi):
    X = lambda time: r * time * np.cos(time + phi)
    Y = lambda time: r * time * np.sin(time + phi)
    return X(time), Y(time)


def theta(omega, t):
    return omega * t


def main():
    n = 200
    omega = np.pi / 6.0
    time = np.linspace(0, 5, n)
    plt.axis('equal')
    X1 = []
    X2 = []
    Y = []
    for i in range(1, 4):
        r = np.abs(np.random.normal(0, 0.2, n)) + 1
        x, y = get_spiral(r, theta(omega, time), -np.pi / 3.0 + i * np.pi * 2.0 / 3.0)
        X1.append(x)
        X2.append(y)
        Y.append(np.ones(x.shape[0]))

        r2 = np.abs(np.random.normal(0, 0.2, n)) + 1
        x2, y2 = get_spiral(r2, theta(omega, time), i * np.pi * 2.0 / 3.0)
        X1.append(x2)
        X2.append(y2)
        Y.append(np.zeros(x2.shape[0]))

    X_tmp1 = np.concatenate((X1[0], X1[1].T), axis=0)
    X_tmp2 = np.concatenate((X1[2], X1[3].T), axis=0)
    X_tmp3 = np.concatenate((X1[4], X1[5].T), axis=0)
    X_sum = np.concatenate((X_tmp1, X_tmp2), axis=0)
    X_total = np.concatenate((X_sum, X_tmp3.T), axis=0)

    X2_tmp1 = np.concatenate((X2[0], X2[1].T), axis=0)
    X2_tmp2 = np.concatenate((X2[2], X2[3].T), axis=0)
    X2_tmp3 = np.concatenate((X2[4], X2[5].T), axis=0)
    X2_sum = np.concatenate((X2_tmp1, X2_tmp2), axis=0)
    X2_total = np.concatenate((X2_sum, X2_tmp3), axis=0)

    Y_tmp1 = np.concatenate((Y[0], Y[1].T), axis=0)
    Y_tmp2 = np.concatenate((Y[2], Y[3].T), axis=0)
    Y_tmp3 = np.concatenate((Y[4], Y[5].T), axis=0)
    Y_sum = np.concatenate((Y_tmp1, Y_tmp2), axis=0)
    Y_total = np.concatenate((Y_sum, Y_tmp3), axis=0)

    raw_data = {
        'x1': X_total,
        'x2': X2_total,
        'y': Y_total,
    }
    df = pd.DataFrame(raw_data, columns=['x1', 'x2', 'y'])
    df.to_csv('ex9.csv')

    dff = pd.read_csv('ex9.csv')
    plt.clf()  # Clear the memory
    plt.axis('equal')
    plt.scatter(dff.x1, dff.x2, c=dff.y)
    plt.savefig('ans.png')
    img = Image.open('ans.png')
    img.show()


if __name__ == '__main__':
    main()
