import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray


def main():
    number = 7
    df = pd.read_csv('../large_files/train.csv')
    M = df.values
    m1 = M[M[:, 0] == number]  # Select label 1
    no_label_m1 = m1[:, 1:]
    row, col = no_label_m1.shape
    sum_1 = np.sum(no_label_m1, axis=0)
    image_sum_1 = sum_1.reshape(28, 28)
    av_sum1 = image_sum_1 / row
    rotate_90 = np.rot90(av_sum1, k=1, axes=(1, 0))

    str_filename = f'm{number}.png'
    plt.imshow(rotate_90, cmap='gray')
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


if __name__ == '__main__':
    main()