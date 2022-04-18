# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
def getData():
    # from bs4 import BeautifulSoup
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://famobi.com/?locale=en', params=payload)
    r.encoding = 'utf-8'
    file_handle=open('./1.html',mode='a') 
    # file_handle.writelines(r.text)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    i = 0
    # file_handle.writelines(soup.find('section', class_="categories").string)
    arrayList = soup.find('section', class_="categories").find_all('li')
    # for link in arrayList:
    #     # tag = BeautifulSoup(link.string).li.section
    #     print(link.a['href'])
    #     c = requests.get('https://famobi.com/' + link.a['href'] + '?locale=en', params=payload)
    #     c.encoding = 'utf-8'
    #     cSoup = BeautifulSoup(c.text)
    #     cDocText = cSoup.find('article', class_="dark").find('div', class_="inner").ul
    #     print(cDocText)
    c = requests.get('https://famobi.com/arcade/?locale=en', 'html.parser')
    c.encoding = 'utf-8'
    cSoup = BeautifulSoup(c.text)
    # cDocText = cSoup.find('article', class_="dark").find('div', class_="inner").ul
    print(cSoup)
    file_handle.writelines(c.text)
getData()