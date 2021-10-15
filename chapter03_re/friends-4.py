import os, re, codecs

f = codecs.open(r'd:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter03\friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

print(re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6])
