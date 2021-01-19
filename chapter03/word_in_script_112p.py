import os, re

os.chdir(r'D:\VisualStudioCode\Python\Doit_living_programming\chapter03')
f = open('friends101.txt', 'r')

sentences = f.readlines()

lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i)]
print(lines[:10])

would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
print(would)

take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]
print(take)

for i in take:
    print(i)

newf = open('would.txt', 'w')
newf.writelines(would)
newf.close()

f.close()
