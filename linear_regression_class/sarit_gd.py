import matplotlib
import numpy as np

matplotlib.use('TkAgg')


def j(w1, w2):
    """
    `surface3d_demo.py`
    https://academo.org/demos/3d-surface-plotter/?expression=x*x-y*y*y*y&xRange=-50%2C+50&yRange=-50%2C+50&resolution=25
    It is like a saddle shape
    :param w1:
    :param w2:
    :return:
    """
    return w1 ** 2, w2 ** 4


def dj(w):
    return np.array([2 * w[0], 4 * w[1] ** 3])


def main2():
    w_vector = np.array([0.75, 0.75])  # Let life start with good starting point
    for i in range(100):
        print(w_vector)
        w_vector = w_vector - 0.445 * dj(w_vector)


def main():
    w1 = 0.75
    w2 = 0.75
    eta = 0.445
    for i in range(100):
        w1 -= eta * 2 * w1
        w2 -= eta * 4 * (w2 ** 3)
        print(w1, w2)

if __name__ == '__main__':
    main2()
