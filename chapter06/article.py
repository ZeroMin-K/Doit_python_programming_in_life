import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

# class값이 item_issue인 <div> 태그의 내용만 추출
#soup.find_all('div', {"class": "item_issue"})

# 위 내용 반복문으로 츨력
# for i in soup.find_all('div', {"class": "item_issue"}):
#     print(i.text)


# # a태그에서 href 속성값 출력 
# for i in soup.find_all('a')[:5]:
# 	i.get('href')

# find_all로 <a> 태그 추출
for i in soup.find_all('div', {"class" : "item_issue"}):
    print(i.find_all('a'))

# # get으로 href 속성값 구하기 => 오류 발생 
# for i in soup.find_all('div', {"class": "item_issue"}):
#     i.find_all('a').get('href')

# <a> 태그모은 리스트의 첫번째 원소만가져와 get사용하여 href 속성값 출력
for i in soup.find_all('div', {"class" : "item_issue"}):
    print(i.find_all('a')[0])

# <a> 태그모은 리스트의 첫번째 원소만가져와 get사용하여 href 속성값 출력
for i in soup.find_all('div', {"class" : "item_issue"}):
    print(i.find_all('a')[0].get('href'))
