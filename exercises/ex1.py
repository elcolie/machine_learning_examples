import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def main():
    A = np.array([
        [0.3, 0.6, 0.1],
        [0.5, 0.2, 0.3],
        [0.4, 0.1, 0.5]
    ])
    v = np.array([1 / 3, 1 / 3, 1 / 3])
    i = 0
    distance = []
    while i < 25:
        v_prime = v.dot(A)
        euclidean_distance = np.linalg.norm(v_prime - v)
        v = v_prime
        i += 1
        print(f"{i}: {v_prime} {euclidean_distance}")
        distance.append(euclidean_distance)
    plt.plot(distance)
    plt.savefig('ex1.png')
    img = Image.open('ex1.png')
    img.show()


if __name__ == '__main__':
    main()
