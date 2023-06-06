import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.pylab as mp

# == Test Round 1 STR ==
""" 
# 20220607 檔案路徑不對
#TRD_Index = pd.read_table('.\_EXAMPLES\part2\index.csv', sep = '\t')

TRD_Index = pd.read_table('index.csv', sep = '\t')
TRD_Index.index = pd.to_datetime(TRD_Index.Date)
Taiex = TRD_Index[TRD_Index.CoName == 'TSE Taiex    '] # 注意要有4個半形空白(因為資料內容有4個空白)

#print(Taiex)

# 繪製台灣加權指數收益率的直方圖
TaiexRet = Taiex.ROI.astype(np.float64)
#TaiexRet.hist()
#plt.show()

# 求出台灣加權指數的收益率的均值
mu = TaiexRet.mean()
sigma = TaiexRet.std()
plt.hist(TaiexRet, density = True)
plt.plot(np.arange(-4, 4, 0.002), stats.norm.pdf(np.arange(-4, 4, 0.002), mu, sigma))
#plt.show()

# 進行區間估計
print(stats.t.interval(0.95, len(TaiexRet) - 1, mu, stats.sem(TaiexRet)))
"""
# == Test Round 1 END ==



# == Test Round 2 STR ==
x = 5
theOutcomes = np.random.binomial(3, 0.5, 500)
print("白努利分佈：", theOutcomes)

theArray = [0,0,0,0]
for outcome in theOutcomes :
    theArray[outcome] += 1

print(theArray)




#x = np.random.binomial(n=5, p=0.5, size=15)
#print("size 10 : ", x)
#print("x/10 : ", x/15)
#print(stats.binom.pmf(5, 10, 0.5))


# 
#sns.distplot(np.random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
#plt.show()

# == Test Round 2 END ==


# == Test Round 3 STR==
""" 
outcomes = np.random.binomial(9, 0.5, 10000)  # 记录成功曲线的数据
chips = [1000]  #记录筹码的变化
for outcome in outcomes:
    if outcome >= 5 :
        chips.append(chips[-1]+1)  # 则将最后一个筹码+1
    else:
        chips.append(chips[-1] - 1)
chips = np.array(chips)  # 变成数组


# 基本图形参数
mp.figure('Binomial', facecolor='lightgray')
mp.title('Binomial', fontsize=20)
mp.xlabel("Round", fontsize=14)
mp.ylabel('Chip', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制图像
if chips[-1] < chips[0]:  # 小于最开始的筹码数，就是输了
    color = 'orangered'
elif chips[-1] > chips[0]:  # 赢了
    color = 'limegreen'
else:
    color = 'dodgerblue'
mp.plot(chips, c=color, label='Chip')

mp.show()
"""
# == Test Round 3 END ==
