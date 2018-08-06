import operator

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray


def main():
    n = 1000
    X = 2 * np.random.random(n) - 1
    Y = 2 * np.random.random(n) - 1
    for x, y in zip(X, Y):
        if x * y < 0:
            plt.scatter(x, y, color='r')
        else:
            plt.scatter(x, y, color='b')
    str_filename = '2d-uniform.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


if __name__ == '__main__':
    main()
