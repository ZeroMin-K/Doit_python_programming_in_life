import os, re

f = open(r'd:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter03\friends101.txt', 'r', encoding = 'utf-8')
# print(f.read(100))
# print(f.seek(0))

sentences = f.readlines()
# print(sentences[:3])

# for i in sentences[:20]:
#     if re.match(r'[A-Z][a-z]+:', i):
#         print(i)

# lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
# print(lines[:10])

# would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
# print(would)

# take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
# # print(take)

# for i in take:
#     print(i)

would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()
