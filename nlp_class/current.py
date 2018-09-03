import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB


def prepare_data():
    data = pd.read_csv('spambase.data').values
    np.random.shuffle(data)

    X = data[:, :48]
    Y = data[:, -1]

    Xtrain = X[:-100, ]
    Ytrain = Y[:-100, ]
    Xtest = X[-100:, ]
    Ytest = Y[-100:, ]
    return Xtrain, Ytrain, Xtest, Ytest


def naive_bayes(Xtrain, Ytrain, Xtest, Ytest):
    model = MultinomialNB()  # Naive Bayes
    model.fit(Xtrain, Ytrain)
    print(f"Classification rate for NB: {model.score(Xtest, Ytest)}")


def ensemble_method(Xtrain, Ytrain, Xtest, Ytest):
    model = AdaBoostClassifier()  # Naive Bayes
    model.fit(Xtrain, Ytrain)
    print(f"Classification rate for NB: {model.score(Xtest, Ytest)}")


def main():
    Xtrain, Ytrain, Xtest, Ytest = prepare_data()
    naive_bayes(Xtrain, Ytrain, Xtest, Ytest)
    ensemble_method(Xtrain, Ytrain, Xtest, Ytest)


if __name__ == '__main__':
    main()
