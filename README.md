## py-django-demo

## 筆記

操作版本資訊
> python = 2.7.6 , django = 1.11.18

> python3.6 = 3.6.3 , django = 2.1.5

啟用服務
 > sudo python src/manage.py runserver $IP:$PORT
    
 > sudo python3.6 src/manage.py runserver $IP:$PORT
 
新增App目錄
 > python src/manage.py startapp AppName
 
新增model 
 > sudo python3.6 src/manage.py makemigrations appName

同步Model to sqlite3
 > sudo python3.6 src/manage.py migrate
    
創建AdminUser
 > sudo python src/manage.py createsuperuser
 
## 參考

Django基礎概念和MVT架構
 > https://hk.saowen.com/a/fbc2bc5a84117a1d3aa144a05c71805320cedbb746642297dd72f35ba03e8dcf

DRF從無到有
 > https://github.com/twtrubiks/django-rest-framework-tutorial

簡易配置js css
 > http://hugo-python3.blogspot.com/2014/03/django-static-file-template-inclde.html
 
