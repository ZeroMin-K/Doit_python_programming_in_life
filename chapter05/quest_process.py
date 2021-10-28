import os, usecsv
import numpy as np

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter05')
quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))
print(quest)

print(quest[quest > 5])
quest[quest > 5] = 5
print(quest)

usecsv.writecsv('resultcsv.csv', list(quest))

result = np.array(usecsv.switch(usecsv.opencsv('resultcsv.csv')))
print(result)
