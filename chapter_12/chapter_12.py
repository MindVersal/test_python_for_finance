import datetime as dt
import numpy as np
import pandas as pd
import pickle
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from chapter_11.chapter_11 import extract_featuresets
from collections import Counter


def test_zero():
    print('Chapter 12')


def test_last():
    print('THE END.')


def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)
    # clf = neighbors.KNeighborsClassifier()
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy ', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread: ', Counter(predictions))
    return confidence


if __name__ == '__main__':
    test_zero()
    do_ml('BAC')
    test_last()
