import pandas as pd
import re, os

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter05')

df = pd.read_csv('apt.csv', encoding = 'cp949')
# print(len(df))

# print(df.head())
# print(df.tail())

# print(df.지역)

# print(df.면적 > 130)
# print(df[df.면적 > 130])
# print(df.가격[(df.면적 > 130) & (df.가격 < 15000)])

# print(df.loc[:10, ['아파트', '가격']])
# print(df.loc[:, ['아파트', '가격']] [df.가격 > 40000])

# df['단가'] = df.가격 / df.면적
# print(df.loc[:10, ('가격', '면적', '단가')])

# print(df.sort_values(by = '가격').loc[:, ('가격', '지역')])
# print(df.sort_values(by = '가격', ascending = False).loc[:, ('가격', '지역')])
# print(df[df.가격 > 40000].sort_values(by = '면적').loc[:, ('가격', '면적', '지역')])

# print(df.지역.str.find('강릉'))

print(df[df.지역.str.find('강릉') > -1])
