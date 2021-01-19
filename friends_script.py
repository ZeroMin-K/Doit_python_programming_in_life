import os, re, codecs

os.chdir(r'D:\VisualStudioCode\Python\Doit_living_programming\chapter03')
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

# Monica 대사 리스트
Line = re.findall(r'Monica:.+', script101)

f = open('monica.txt', 'w', encoding = 'utf-8')

monica = ''
for i in Line:
    monica += i

f.write(monica)

f.close()