import datetime as dt
import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


def test_zero():
    print('Chapter 00')


def test_last():
    print('THE END.')


def test_chapter_00():
    style.use('ggplot')
    quandl.ApiConfig.api_key = 'BcPAXwup9YZoTCZsDAhx'
    start_date = dt.datetime(1900, 1, 1)
    end_date = dt.datetime(2017, 9, 9)
    df = quandl.get('WIKI/AAPL', start_date=start_date, end_date=end_date)
    daily_close = df[['Adj. Close']]
    # daily_close.plot()
    daily_pct_change = daily_close.pct_change()
    daily_pct_change.fillna(0, inplace=True)
    # daily_pct_change.plot()
    daily_log_returns = np.log(daily_close.pct_change() + 1)
    cum_daily_returns = (1 + daily_pct_change).cumprod()
    # cum_daily_returns.plot()

    tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
    all_data = get_all_data(tickers, dt.datetime(2017, 9, 1), dt.datetime(2017, 9, 9))
    print(all_data['Adj. Close'].tail(25))

    plt.show()


def get_all_data(tickers, start_date, end_date):
    def data(ticker):
        return quandl.get('WIKI/{}'.format(ticker), start_date=start_date, end_date=end_date)
    datas = map(data, tickers)
    return pd.concat(datas, keys=tickers, names=['Ticker', 'Date'])


if __name__ == '__main__':
    test_zero()
    test_chapter_00()
    test_last()
