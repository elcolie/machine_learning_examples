import matplotlib.pyplot as plt
import numpy as np


def rbool(x: float):
    return x > 0


def xor(x: bool, y: bool) -> bool:
    return x != y


def main():
    pp = np.random.uniform(-1, 1, (1000, 2))
    tmp = rbool(pp)
    tmp2 = xor(tmp[:, 0], tmp[:, 1])

    col = lambda x: 'r' if x else 'b'
    vfunc = np.vectorize(col)
    ans = vfunc(tmp2)

    plt.scatter(pp[:, 0], pp[:, 1], c=ans)
    str_filename = '2d-uniform.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


if __name__ == '__main__':
    main()
