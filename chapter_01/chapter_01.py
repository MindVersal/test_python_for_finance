import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


def test_zero():
    print('Programming on python for finance.')


def test_last():
    print('THE END.')


def test_tsla_yahoo():
    style.use('ggplot')
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2012, 12, 31)
    df = web.DataReader('TSLA', 'google', start, end)
    print(df.tail(6))


if __name__ == '__main__':
    test_zero()
    test_tsla_yahoo()

    test_last()
