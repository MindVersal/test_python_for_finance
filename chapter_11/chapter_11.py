import datetime as dt
import numpy as np
import pandas as pd
import pickle
from collections import Counter
from chapter_09.chapter_09 import process_data_for_labels
from chapter_10.chapter_10 import buy_sell_hold


def test_zero():
    print('Chapter 11')


def test_last():
    print('THE END.')


def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]
                                              ))
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    # print('Data spread: ', Counter(str_vals))
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    X = df_vals.values
    y = df['{}_target'.format(ticker)].values
    return X, y, df


if __name__ == '__main__':
    test_zero()
    extract_featuresets('XOM')
    test_last()
