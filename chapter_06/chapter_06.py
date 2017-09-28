import datetime as dt
import pandas as pd
import bs4 as bs
import pickle
import requests
import os
import quandl


def test_zero():
    print('Chapter 06')


def test_last():
    print('THE END.')


def test_get_data_from_web():
    with open('../sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    if not os.path.exists('../stock_dfs'):
        os.makedirs('../stock_dfs')
    quandl.ApiConfig.api_key = 'BcPAXwup9YZoTCZsDAhx'
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('../stock_dfs/{}.csv'.format(ticker)):
            df = quandl.get('WIKI/{}'.format(ticker), start_date=start, end_date=end)
            df.to_csv('../stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


if __name__ == '__main__':
    test_zero()
    test_get_data_from_web()
    test_last()
