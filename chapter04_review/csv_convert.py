import os, re
import usecsv

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
total = usecsv.opencsv('popSeoul.csv')

# for i in total[:5]:
#     print(i)

# j = '1,468,146'
# print(float(re.sub(',', '', j)))
# print(type(float(re.sub(',', '', j))))

# import re
# i = total[2]

# k = []
# for j in i:
#     # 숫자가 들어있다면
#     if re.search('\d', j):
#         # 쉼표 삭제후 실수형으로 바꿈
#         k.append(float(re.sub(',', '', j)))
#     else:
#         k.append(j)

# print(k)

# import re

# p = ['123강남', '151,767', '11,039', '12,1235']
# k = []
# for j in p:
#     if re.search('\d', j):
#         k.append(float(re.sub(',', '', j)))
#     else:
#         k.append(j)

# print(k)

# import re

# p = ['123강남', '151,767', '11,039', '12,1235']
# k = []

# for j in p:
#     if re.search('[a-z가-힣]', j):
#         k.append(j)
#     else:
#         k.append(float(re.sub(',', '', j)))

# print(k)


# import re

# p = ['123!!', '151,767', '11,039', '12,1235']
# k = []

# for j in p:
#     if re.search('[a-z가-힣!]', j):
#         k.append(j)
#     else:
#         k.append(float(re.sub(',', '', j)))

# print(k)


import re

i = ['123!!', '151,767', '11,039', '12,1235']

for j in i:
    if re.search('[a-z가-힣!]', j):
        i[i.index(j)] = j
    else:
        i[i.index(j)] = (float(re.sub(',', '', j)))

print(i)
