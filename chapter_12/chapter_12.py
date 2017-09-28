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
    # print('{} Accuracy {}'.format(ticker, confidence))
    predictions = clf.predict(X_test)
    print('{} Predicted spread: {}'.format(ticker, Counter(predictions)))
    return Counter(predictions)


def test_sells():
    with open('../sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    tickers_clear = []
    for ticker in tickers:
        ml_responce = do_ml(ticker)
        tickers_clear.append({'ticker': ticker, '0': ml_responce[0], '1': ml_responce[1], '-1': ml_responce[-1]})
    ticker_for_sell = []
    ticker_for_buy = []
    count_positions = 1066
    count_relevant = count_positions // 2
    for ticker in tickers_clear:
        if ticker['1'] > count_relevant:
            ticker_for_buy.append(ticker)
        if ticker['-1'] > count_relevant:
            ticker_for_sell.append(ticker)
    print('Tickets for BUY: {}'.format(ticker_for_buy))
    print('Tickets for SELL: {}'.format(ticker_for_sell))


if __name__ == '__main__':
    test_zero()
    test_sells()
    test_last()
