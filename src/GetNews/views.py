#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from GetNews.apps import getNews
# Create your views here.
def home(request):
    return HttpResponse("<p>Hello FatZai Xuan!</p>")
    
def GetNews(request):
    Msg = getNews()
    return HttpResponse(Msg)
 