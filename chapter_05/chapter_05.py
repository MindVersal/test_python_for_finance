import bs4 as bs
import pickle
import requests
import quandl
import datetime as dt

def test_zero():
    print('Chapter 05')


def test_last():
    print('THE END.')


def test_save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    un_tickers = ('BRK.B', 'BF.B')
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        if ticker in un_tickers:
            continue
        tickers.append(ticker)
    with open('../sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    print(tickers)
    return tickers


def test_load_from_quandl():
    quandl.ApiConfig.api_key = 'BcPAXwup9YZoTCZsDAhx'
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2012, 12, 31)
    tsla_prices = quandl.get('WIKI/TSLA', start_date=start, end_date=end)
    print(tsla_prices[['Open', 'Close', 'Volume']])


if __name__ == '__main__':
    test_zero()
    test_save_sp500_tickers()
    # test_load_from_quandl()
    test_last()
