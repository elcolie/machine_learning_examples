import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray


def single_image(M: ndarray):
    """Show single image of number 1"""
    m1 = M[M[:, 0] == 1]  # Select label 1
    single_no_label_m1 = m1[0, 1:]  # Remove label
    im = single_no_label_m1.reshape(28, 28)
    plt.imshow(255 - im, cmap='gray')
    plt.savefig('im.png')
    from PIL import Image
    img = Image.open('im.png')
    img.show()


def average_image(number: int, M: ndarray):
    """Show average of given number"""
    m1 = M[M[:, 0] == number]  # Select label 1
    no_label_m1 = m1[:, 1:]
    row, col = no_label_m1.shape
    sum_1 = np.sum(no_label_m1, axis=0)
    image_sum_1 = sum_1.reshape(28, 28)
    av_sum1 = image_sum_1 / row
    plt.imshow(av_sum1, cmap='gray')
    str_filename = f'm{number}.png'
    plt.savefig(str_filename)
    from PIL import Image
    img = Image.open(str_filename)
    img.show()


def main():
    df = pd.read_csv('../large_files/train.csv')
    M = df.values
    average_image(7, M)


if __name__ == '__main__':
    main()
