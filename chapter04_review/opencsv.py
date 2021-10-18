import csv, os

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)

    return output

if __name__ == '__main__':
    os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter04')
    print(opencsv('example2.csv'))
