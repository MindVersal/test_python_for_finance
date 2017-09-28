import datetime as dt
import numpy as np
import pandas as pd
import pickle


def test_zero():
    print('Chapter 09')


def test_last():
    print('THE END.')


def process_data_for_labels(ticker):
    hm_days = 7
    df = pd.read_csv('../sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)
    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]
    df.fillna(0, inplace=True)
    return tickers, df


def test_chapter_09():
    print(process_data_for_labels('XOM'))


if __name__ == '__main__':
    test_zero()
    test_chapter_09()
    test_last()
