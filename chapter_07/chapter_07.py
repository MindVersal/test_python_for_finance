import datetime as dt
import pickle
import bs4 as bs
import requests
import pandas as pd
import os


def test_zero():
    print('Chapter 07')


def test_last():
    print('THE END.')


def test_compile_data():
    with open('../sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers):
        if count % 10 == 0:
            print(count)
        if not os.path.exists('../stock_dfs/{}.csv'.format(ticker)):
            continue
        df = pd.read_csv('../stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj. Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split Ratio',
                 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume'], 1, inplace=True)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

    print(main_df.head())
    main_df.to_csv('../sp500_joined_closes.csv')


if __name__ == '__main__':
    test_zero()
    test_compile_data()
    test_last()
