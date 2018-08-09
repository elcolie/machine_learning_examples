import matplotlib.pyplot as plt
import numpy as np


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

    for i in range(1, 4):
        r = np.abs(np.random.normal(0, 0.2, n)) + 1
        x, y = get_spiral(r, theta(omega, time), -np.pi / 3.0 + i * np.pi * 2.0 / 3.0)
        plt.scatter(x, y, c='blue')

        r2 = np.abs(np.random.normal(0, 0.2, n)) + 1
        x2, y2 = get_spiral(r2, theta(omega, time), i * np.pi * 2.0 / 3.0)
        plt.scatter(x2, y2, c='red')

    str_filename = 'ex8.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


if __name__ == '__main__':
    main()
