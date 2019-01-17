#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.apps import AppConfig
from bs4 import BeautifulSoup
import requests as rq

class TestsqlConfig(AppConfig):
    name = 'TestSQL'

def getNews():
    
    #url = 'https://nba.udn.com/nba/cate/6754'
    url = GetNewsUrl()
    basicUrl = 'https://nba.udn.com/'
    response = rq.get(url) 
    html_doc = response.text 
    soup = BeautifulSoup(response.text)
    soup1 = soup.find(id="news_list")
    Test = soup1.findAll("dt")
    NewsShow =""
    for item in Test:
        #print(item)
        #print('\r\nTitle:' + item.h3.text)
        #print('NewsURL:' + item.a['href'])
        #print('ImgURL:' + item.img['data-src'])
        #print('Content:' + item.p.text)
        NewsShow += "標題:"  + item.h3.text.encode('utf-8') + "<br/>"
        NewsShow += "時間:"  + item.b.text.encode('utf-8') + "<br/>"
        NewsShow += "網頁Url:<a href='"+ basicUrl  +  item.a['href'].encode('utf-8') + "'>新聞連結</a><br/>"
        NewsShow += "簡述:"  +  item.p.text.encode('utf-8') + "<br/>"
        NewsShow += "<img src='"  +  item.img['data-src'].encode('utf-8') + "'></img><br/><hr/>"
    return NewsShow
    
def GetNewsUrl():
    url = 'https://nba.udn.com/nba/index'
    response = rq.get(url) 
    html_doc = response.text 
    soup = BeautifulSoup(response.text)
    soup1 = soup.find(id="mainbar")
    soup2 = soup1.findAll("h1", {"class": "box-title"})
    return 'https://nba.udn.com/' + soup2[0].a['href']

    