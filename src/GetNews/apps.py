#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.apps import AppConfig
from bs4 import BeautifulSoup
import requests as rq
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

class TestsqlConfig(AppConfig):
    name = 'TestSQL'
    
def getNewsRawData():
    url = getNewsUrl()
    response = rq.get(url) 
    html_doc = response.text 
    soup = BeautifulSoup(response.text, 'html.parser')
    soup1 = soup.find(id="news_list")
    return soup1.findAll("dt")
    
def showNews():
    basicUrl = 'https://nba.udn.com/'
    Test = getNewsRawData()
    NewsShow =""
    for item in Test:
        NewsShow += "標題:"  + str(item.h3.text) + "<br/>"
        NewsShow += "發表時間:"  +  getNewsPublishTime(basicUrl+ str(item.a['href'])) + "<br/>"
        NewsShow += "時間:"  + str(item.b.text) + "<br/>"
        NewsShow += "網頁Url:<a href='"+ basicUrl  +  str(item.a['href']) + "'>新聞連結</a><br/>"
        NewsShow += "簡述:"  +  str(item.p.text) + "<br/>"
        NewsShow += "<img src='"  +  str(item.img['data-src']) + "'></img><br/><hr/>"
    return NewsShow
    
def getNewsPublishTime(url):
    
    response = rq.get(url) 
    html_doc = response.text 
    soup = BeautifulSoup(response.text, 'html.parser')
    soup1 = soup.findAll("div", {"class": "shareBar__info--author"})
    return str(soup1[0].span.text)
    
def getNewsUrl():
    url = 'https://nba.udn.com/nba/index'
    response = rq.get(url) 
    html_doc = response.text 
    soup = BeautifulSoup(response.text, 'html.parser')
    soup1 = soup.find(id="mainbar")
    soup2 = soup1.findAll("h1", {"class": "box-title"})
    return 'https://nba.udn.com/' + soup2[0].a['href']


    