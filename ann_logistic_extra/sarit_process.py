import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

"""
1. is_mobile,  
2. n_products_viewed,   
3. visit_duration, 
4. is_returning_visitor,   
5. time_of_day,
    
user_action
"""


def get_data():
    df = pd.read_csv('ecommerce_data.csv')
    data = df.values

    X = data[:, :-1]  # X is everything except last column
    Y = data[:, -1]  # Y is the only last column

    # Normalization `n_products and visit_duration`
    X[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    X[:, 2] = (X[:, 2] - X[:, 2].mean()) / X[:, 2].std()

    # Next is work on time of the day
    N, D = X.shape
    X2 = np.zeros((N, D + 3))  # Just 3 is enough since `time_of_day` will be reused
    X2[:, 0:(D - 1)] = X[:, 0:(D - 1)]  # Create a new one by copy the existing one

    for n in range(N):
        tt = int(X[n, D - 1])
        X2[n, tt + D - 1] = 1  # Translation the column and set equals to 1

    Z = np.zeros((N, 4))
    Z[np.arange(N), X[:, D - 1].astype(np.int32)] = 1

    assert (np.abs(X2[:, -4:] - Z).sum() < 10e-10)
    return X2, Y


def get_binary_data():
    X, Y = get_data()
    X2 = X[Y <= 1]
    Y2 = Y[Y <= 1]
    return X2, Y2


