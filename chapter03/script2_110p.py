import os, re, codecs

os.chdir(r'D:\VisualStudioCode\Python\Doit_living_programming\chapter03')
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

script = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6]
print(script)