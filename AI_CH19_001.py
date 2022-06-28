import pandas as pd
import numpy as np

stock = pd.read_csv('2330.csv', index_col = 'Date', sep = '\t')
close = stock.Close
print(close.head())

close.index = pd.to_datetime(close.index)
lagclose = close.shift(1)
# 計算單期簡單收益率
simpleret = (close - lagclose) / lagclose
simpleret.name = 'simpleret'
print(simpleret.head())

# 計算2期簡單收益率
simpleret2 = (close -close.shift(2)) / close.shift(2)
simpleret2.name = 'simpleret2'
print(simpleret2.head())
