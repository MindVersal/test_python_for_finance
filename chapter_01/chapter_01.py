import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as pdr


def test_zero():
    print('Programming on python for finance.')


def test_last():
    print('THE END.')


def test_tsla_download():
    style.use('ggplot')
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2012, 12, 31)
    df = pdr.get_data_google('TSLA')
    df.to_csv('../tsla.csv')
    print(df.head(6))


if __name__ == '__main__':
    test_zero()
    test_tsla_download()

    test_last()
