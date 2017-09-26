import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


def test_zero():
    print('Chapter_03')


def test_last():
    print('THE END.')


def test_mean():
    style.use('ggplot')
    df = pd.read_csv('../tsla.csv', parse_dates=True, index_col=0)
    df['100ma'] = df['Close'].rolling(window=100).mean()
    df.dropna(inplace=True)
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    ax1.plot(df.index, df['Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])

    # df[['Close', '100ma']].plot()
    plt.show()


if __name__ == '__main__':
    test_zero()
    test_mean()

    test_last()
