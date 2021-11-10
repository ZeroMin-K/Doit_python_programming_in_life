import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

os.chdir(r'D:\VisualStudioCode\Python\Do_it_Python_Programming_in_Life\chapter06')
news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')
# print(soup)

# print(soup.find_all('div', {'class' : 'item_issue'}))

# for i in soup.find_all('div', {'class' : 'item_issue'}):
#     print(i.text)

# print(soup.find_all('a'))

# for i in soup.find_all('a')[:5]:
#     print(i.get('href'))

# for i in soup.find_all('div', {'class': 'item_issue'}):
#     print(i.find_all('a'))

# for i in soup.find_all('div', {'class': 'item_issue'}):
#     print(i.find_all('a').get('href'))

# for i in soup.find_all('div', {'class': 'item_issue'}):
#     print(i.find_all('a')[0])

# for i in soup.find_all('div', {'class' : 'item_issue'}):
#     print(i.find_all('a')[0].get('href'))

# article1 = 'https://news.v.daum.net/v/20211109213509205'
# soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

# for i in soup2.find_all('p'):
#     print(i.text)

# headline = soup.find_all('div', {'class' : 'item_issue'})
# print(headline[0].text)

# headline = soup.find_all('div', {'class' : 'item_issue'})
# for i in headline:
#     print(i.text, '\n')

# for i in headline:
#     print(i.text, '\n')

#     soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')

#     for j in soup3.find_all('p'):
#         print(j.text)

# f = open('links.txt', 'w')
# for i in soup.find_all('div', {'class' : 'item_issue'}):
#     f.write(i.find_all('a')[0].get('href') + '\n')

# f.close()

# article1 = 'https://news.v.daum.net/v/20211109213509205'
# soup2 = bs(ur.urlopen(article1).read(), 'html.parser')
# f = open('article_1.txt', 'w')
# for i in soup.find_all('p'):
#     f.write(i.text) 
# f.close()

url = 'https://news.daum.net/'
soup = bs(ur.urlopen(url).read(), 'html.parser')
f = open('article_total.txt', 'w')
for i in soup.find_all('div', {'class' : 'item_issue'}):
    try:
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')    
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()
