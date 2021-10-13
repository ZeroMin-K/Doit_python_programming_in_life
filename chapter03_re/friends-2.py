import os, re, codecs

f = codecs.open(r'd:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter03\friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()


Line = re.findall(r'Monica:.+', script101)
# print(Line[:3])

# for item in Line[:3]:
#     print(item)

# f.close()

# f = open('monica.txt', 'w', encoding = 'utf-8')

# monica = ''

# for i in Line:
#     monica += i

# print(f.write(monica))

# f.close()

monica = ''
for i in Line:
    monica += i + '\n'

print(monica[:100])

f = open('monica.txt', 'w', encoding = 'utf-8')
f.write(monica)
f.close() 
