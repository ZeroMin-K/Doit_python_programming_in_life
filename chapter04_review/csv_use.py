a = [['구', '전체', '내국인', '외국인'],
['관악구', '519864', '502080', '18885'],
['강남구', '547602', '542498', '5104'],
['송파구', '686161', '679472', '6934'],
['강동구', '428547', '424235', '412']]

import csv, os
os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
f = open('abc.csv', 'w', newline = '')

csvobject = csv.writer(f, delimiter = ',')

csvobject.writerows(a)
f.close()
