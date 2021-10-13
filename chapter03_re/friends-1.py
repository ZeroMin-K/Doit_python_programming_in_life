import os, re, codecs

f = codecs.open(r'd:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter03\friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

print(script101[:100])
