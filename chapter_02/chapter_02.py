from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr


def test_zero():
    print('Chapter 02')


def test_last():
    print('THE END.')


def test_csv():
    style.use('ggplot')
    df = pd.read_csv('../tsla.csv', parse_dates=True, index_col=0)
    print(df[['Open', 'High']].head())
    df['Close'].plot()
    plt.show()


if __name__ == '__main__':
    test_zero()
    test_csv()
    test_last()
