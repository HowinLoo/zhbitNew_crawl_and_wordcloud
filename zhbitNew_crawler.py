# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:13:45 2017

@author: Howin
"""

import requests
from bs4 import BeautifulSoup
import re, time, random

url = 'http://zhbit.com/important'
url0 = 'http://zhbit.com/important'
urlIndex = 'http://zhbit.com/important/index_{}.html'
url_header = 'http://zhbit.com'
filepath = 'D:/Dairly/Code/PY/爬虫/zhbitNew/{}.txt'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36',
           'Connection':'close'}
proxy = {'http':'192.168.191.23:8118'}
page = 0
requests.adapters.DEFAULT_RETRIES = 50
s = requests.session()
s.keep_alive = False


for i in range(78):
    urlList = []
    if page == 0:
        url = url0
        page = 1
        print('>>>Now robot crawls the %d page'%page)
    else:
        page += 1
        print('>>>Now robot crawls the %d page'%page)
        url = urlIndex.format(page)
    rPage = requests.get(url, headers = headers, verify=False)
    soup = BeautifulSoup(rPage.text, 'html.parser')
    b_list = soup.find('div','b_list')
    soup_url = BeautifulSoup(str(b_list),'html.parser')
    a_href = soup_url('a')
    time.sleep(random.random())
    #rPage.connection.close()
    for href_url in a_href:
        urlList.append(url_header+href_url['href'])
    for i in range(len(urlList)):
        try:
            rNew = requests.get(urlList[i], headers = headers, verify=False, timeout = 45)
            rNew.encoding = 'gbk'
            soup_new = BeautifulSoup(rNew.text,'html.parser')
            soup_title = re.sub(r'，|"|/','',soup_new.find('td','t2').string)
            soup_new_pureword = ''.join(soup_new.text.split())
            new_article = re.findall(r'阅读次数：(.*)新闻排行',soup_new_pureword)
            time.sleep(random.random())
            with open(filepath.format(soup_title),'w',encoding = 'utf-8') as file:
                file.write(new_article[0])
                time.sleep(random.random())
        #rNew.connection.close()
        except:
            continue
print('>>>The End,luckly for you')