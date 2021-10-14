import os, re, codecs

f = codecs.open(r'd:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter03\friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

char = re.compile(r'[A-Z][a-z]+:')

# print(re.findall(char, script101))

# print(set(re.findall(char, script101)))

# y = set(re.findall(char, script101))
# z = list(y)
# character = []
# for i in z:
#     character += [i[:-1]]

# print(character)


character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(character)
