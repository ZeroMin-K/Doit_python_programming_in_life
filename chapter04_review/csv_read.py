import csv, os

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
f = open('a.csv', 'r')
# f = open('a.csv', 'r', encoding = 'utf-8')

new = csv.reader(f)

# for i in new:
#     print(i)

a_list = []
for i in new:
    print(i)
    a_list.append(i)

print(a_list)
