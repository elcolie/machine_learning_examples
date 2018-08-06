import matplotlib.pyplot as plt
import numpy as np


def main():
    n = 1000
    R = np.random.random((n, n))
    Y = np.sum(R, axis=1)  # horizontal sum
    plt.hist(Y)
    plt.savefig('gaussian.png')
    from PIL import Image
    img = Image.open('gaussian.png')
    img.show()


if __name__ == '__main__':
    main()
