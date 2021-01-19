import os, re, codecs

os.chdir(r'D:\VisualStudioCode\Python\Doit_living_programming\chapter03')
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

char = re.compile(r'[A-Z][a-z]+:')
y = set(re.findall(char, script101))
z = list(y)
character = []

for i in z:
    character += [i[:-1]]

print(character)

character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:', script101)))]
print(character)
f.close()
