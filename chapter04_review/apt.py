import os, re, usecsv

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
apt = usecsv.switch(usecsv.opencsv('apt_202109.csv'))

# print(apt[:3])
# print(len(apt))

# for i in apt[:6]:
#     print(i[0])

# for i in apt[:6]:
#     print(i[0], i[4], i[-4])

# for i in apt:
#     try:
#         if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
#             print(i[0], i[4], i[-4])

#     except:
#         pass

new_list = []
for i in apt:
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
            new_list.append([i[0], i[4], i[-4]])
    except:
        pass

usecsv.writecsv('over120_lower3000.csv', new_list)
