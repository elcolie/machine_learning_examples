import matplotlib.pyplot as plt
import numpy as np

def get_spiral(r, time):
    X = lambda time: r * time * np.cos(time)
    Y = lambda time: r * time * np.sin(time)
    return X(time), Y(time)

def main():
    n = 200
    omega = 0.5 * np.pi
    time = np.linspace(0, 1, n)
    theta = lambda time: omega * time
    r = np.abs(np.random.normal(0, 0.2, n)) + 1
    x, y = get_spiral(r, theta(time))
    plt.axis('equal')
    plt.scatter(x, y)

    str_filename = 'ex8.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()

if __name__ == '__main__':
    main()
