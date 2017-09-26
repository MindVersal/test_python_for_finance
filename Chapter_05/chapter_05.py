import bs4 as bs
import pickle
import requests


def test_zero():
    print('Chapter 05')


def test_last():
    print('THE END.')


def test_save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    with open('../sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)
    print(tickers)
    return tickers


if __name__ == '__main__':
    test_zero()
    test_save_sp500_tickers()
    test_last()
