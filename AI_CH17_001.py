import pandas as pd
import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols

year_return = pd.read_csv('TRD_Year.csv', encoding = 'big5')

model = ols('Return ~ C(Industry)', data = year_return.dropna()).fit()
table1 = anova.anova_lm(model)
print(table1)