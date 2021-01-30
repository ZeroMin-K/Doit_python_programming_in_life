import csv, os

# os.chdir(r'a.csv 파일이 있는 폴더 경로')

f = open('a.csv', 'r')

new = csv.reader(f)
for i in new:
    print(i)

f.seek(0)

a_list = []
for i in new:
    print(i)
    a_list.append(i)

print(a_list)
