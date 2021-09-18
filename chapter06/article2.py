import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

# 웹문서를 뷰티풀수프 객체에 저장
article1 = 'https://news.v.daum.net/v/20210918215447842'
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

# 다음 뉴스 웹문서를 뷰티풀수프 객체에 저장 
news = 'https://news.daum.net/'
soup = bs(ur.urlopen(news).read(), 'html.parser')

# 기사 내용 가져오기
for i in soup2.find_all('p'):
    print(i.text)

# 기사 제목 가져오기
headline = soup.find_all('div', {"class" : "item_issue"})

# 첫번째 기사의 제목만 추출
print(headline[0].text)

# 기사 제목 전부추출
for i in headline:
    print(i.text, '\n')

# 기사 본문 전부 추출
for i in headline:
    # headline객체에서 <div> 태그 가져옴
    print(i.text, '\n')
    # 기사제목 출력
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')  

    for j in soup3.find_all('p'):
        print(j.text)
