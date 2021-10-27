import re, usecsv, os

english = 'She is a vegetarian. She does not eat meat. She thinks that animals should not be killed.'
korean = '그녀는 채식주의자 입니다. 그녀는 고기를 먹지않습니다. 그녀는 동물을 죽이지 말아야한다고 생각합니다.'

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')

korean_list = re.split('\.',korean)
english_list = re.split('\.', english)

print(korean_list)

total = []

for i in range(len(english_list)):
    total.append([english_list[i], korean_list[i]])

usecsv.writecsv('korean_english.csv', total)
