import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray

def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(np.allclose(A, A.transpose(), atol=1e-8))
    B = np.array([
        [1, 2, 3],
        [2, 1, 0],
        [3, 0, 3],
    ])
    print(np.allclose(B, B.transpose(), atol=1e-8))

if __name__ == '__main__':
    main()