import os, re
import pandas as pd

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter05')

df2 = pd.read_csv('survey.csv')

# print(df2.head())

# print(df2.mean())
# print(df2.income.mean())
# print(df2.income.sum())

# print(df2.income.median())

# print(df2.describe())
# print(df2.income.describe())

# print(df2.sex.value_counts())

print(df2.groupby(df2.sex).mean())
