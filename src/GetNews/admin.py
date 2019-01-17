#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
#因為student定義在models.py，所以需要import來加入該套件
from GetNews.models import News

admin.site.register(News)