import os, re
from typing import ByteString
import requests
import urllib.request as ur 
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/'

# url 객체에 저장된 URL주소에 해당하는 웹상트 불러오기 
# html = ur.urlopen(url)
# soup = bs(html.read(), 'html.parser')

# 위 내용을 한 줄로 만들기 
soup = bs(ur.urlopen(url).read(), 'html.parser')

# span 태그 찾기 
quote = soup.find_all('span')

# 찾은 태그에서 텍스트만 출력
print(quote[0].text)

# 반복문을 이용해 찾은 태그들의 텍스트 전부 출력. 
# for i in quote:
#   print(i.text)

# <div> 태그 안 class가 quote일 때 텍스트만 
# print(soup.find_all('div', {"class" : "quote"})[0].text)

# <div> 태그안 class가 quote일때 텍스트 전부 추출
for i in soup.find_all('div', {"class":"quote"}):
    print(i.text)
