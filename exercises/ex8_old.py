import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cartesian(tx, omega, phi):
    tmp = np.zeros((tx.shape[0], 2))
    tmp[:, 0] = tx * np.cos(omega * tx + phi) + np.random.normal(0, 0.2, tx.shape[0])
    tmp[:, 1] = tx * np.sin(omega * tx + phi) + np.random.normal(0, 0.2, tx.shape[0])

    return tmp


def draw(plt, tx, omega, phi, color: str):
    f1 = cartesian(tx, omega, phi)
    plt.scatter(f1[:, 0], f1[:, 1], c=color)


def main():
    tx = np.linspace(0, 10, num=200)
    for i in range(1, 4):
        draw(plt, tx, np.pi / 6.0, -np.pi / 3.0 + i * np.pi * 2.0 / 3.0, 'r')
        draw(plt, tx, np.pi / 6.0, i * np.pi * 2.0 / 3.0, 'b')
    plt.show()


if __name__ == '__main__':
    main()