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
print("simpleret: " + str(type(simpleret)))

print("== annualize ==")
annualize = (1 + simpleret).cumprod()[-1]
print(annualize)
print("annualize: " + str(type(annualize)))

annualize2 = (1 + simpleret).cumprod()[4]
print(annualize2)
print("annualize2: " + str(type(annualize2)))


# 計算2期簡單收益率
'''
simpleret2 = (close - close.shift(2)) / close.shift(2)
simpleret2.name = 'simpleret2'
print(simpleret2.head())
'''
print("== s ==")
s = pd.Series([0.1, 0.2, 0.3])
print("s: " + str(type(s)))
test_s = (1 + s).cumprod()[-1]
print("test_s: " + str(type(test_s)))
print(test_s)
#print(test_s[-1])

