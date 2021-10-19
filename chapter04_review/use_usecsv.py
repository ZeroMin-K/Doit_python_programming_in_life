import usecsv,os

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
a = [['국어', '영어', '수학'], [99,.99,77]]
usecsv.writecsv('test.csv', a) 
