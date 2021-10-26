import os, re, usecsv

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total) 

# print(newPop[:4])

# i = newPop[1]
# print(i)

# foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
# print(foreign)

# for i in newPop:
#     foreign = 0
#     try:
#         foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
#         print(i[0], foreign)
#     except:
#         pass

# new = [['구', '한국인', '외국인', '외국인 비율(%)']]

# i = newPop[1]
# foreign = round(i[2] / (i[1] + i[2]) * 100, 1)

# new.append([i[0], i[1], i[2], foreign])

# print(new)

# for i in newPop:
#     foreign = 0
#     try:
#         foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
#         if foreign > 3:
#             print([i[0], i[1], i[2], foreign])
#     except:
#         pass 

new = [['구', '한국인', '외국인', '외국인 비율(%)']]

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2] / (i[1] + i[2]) * 100, 1)
        if foreign > 3:
            new.append([i[0], [1], i[2], foreign])
    except:
        pass

usecsv.writecsv('newPop.csv', new)
