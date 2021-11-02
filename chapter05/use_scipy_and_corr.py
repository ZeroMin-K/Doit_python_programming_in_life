import os, re
import pandas as pd

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter05')

df2 = pd.read_csv('survey.csv')

from scipy import stats

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

# print(stats.ttest_ind(male, female))

# ttest_result = stats.ttest_ind(male, female)
# print(ttest_result)

# print(ttest_result[0])
# print(ttest_result[1])

# if ttest_result[1] > .05:
#     print('p-value는 %f로 95%% 수준에서 유의하지 않음' % ttest_result[1])
# else:
#     print('p-value는 %f로 95%% 수준에서 유의함' % ttest_result[1])

# corr = df2.corr()
# print(corr)

# print(df2.corr(method = 'spearman'))

# print(df2.income.corr(df2.stress))

corr = df2.corr()
corr.to_csv('corr.csv')
