import os, re
import usecsv

# i = ['123!!', '151,767', '11,039', '12,1235', '']

# for j in i:
#     if re.search('[a-z가-힣!]', j):
#         i[i.index(j)] = j
#     else:
#         i[i.index(j)] = (float(re.sub(',', '', j)))

# print(i)

i = ['123!!', '151,767', '11,039', '12,1235', '', '!!!$%']

for j in i:
    try: 
        i[i.index(j)] = float(re.sub(',', '', j))
    except:
        pass

print(i)
