import matplotlib.pyplot as plt
import numpy as np


def get_x(r, rho):
    return r * np.cos(rho)


def get_y(r, rho):
    return r * np.sin(rho)


def gen_circle(r, psi):
    x = get_x(r, psi)
    y = get_y(r, psi)
    return x, y


def main():
    """You have to transform the problem in to the correct domain"""
    psi = np.linspace(0, 2 * np.pi, 500)
    r1 = np.random.normal(10, 0.5, 500)
    r2 = np.random.normal(20, 0.5, 500)

    x, y = gen_circle(r1, psi)
    x2, y2 = gen_circle(r2, psi)

    plt.axis('equal')
    plt.scatter(x, y, cmap='red')
    plt.scatter(x2, y2, cmap='blue')

    str_filename = 'test.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


if __name__ == '__main__':
    main()
