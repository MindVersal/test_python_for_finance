import datetime as dt
import numpy as np
import pandas as pd


def test_zero():
    print('Chapter 10')


def test_last():
    print('THE END.')


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.05
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0


if __name__ == '__main__':
    test_zero()
    buy_sell_hold()
    test_last()
