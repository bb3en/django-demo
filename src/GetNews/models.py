#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models


class News(models.Model):
    Serial = models.CharField(max_length=256, verbose_name='流水號')
    group_id = models.CharField(max_length=256, verbose_name='組序號')
    img_url = models.CharField(max_length=256, verbose_name='圖片網址')
    title = models.CharField(max_length=50, verbose_name='標題')
    content = models.TextField(verbose_name='簡述')
    time = models.TimeField(verbose_name='發表時間')
    def __unicode__(self): 
        return self.Serial