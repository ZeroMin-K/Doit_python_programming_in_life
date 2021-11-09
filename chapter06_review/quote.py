import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com'
# html = ur.urlopen(url)
# print(html.read()[:100])

html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

# print(soup)
# print(type(html))
# print(type(soup))

# soup.find_all('span')

# quote = soup.find_all('span')
# print(quote[0])
# print(quote[0].text)

# for i in quote:
#     print(i.text)

# print(soup.find_all('div', {'class' : 'quote'})[0])
print(soup.find_all('div', {'class' : 'quote'})[0].text)
