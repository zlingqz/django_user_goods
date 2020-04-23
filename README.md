# django_user_goods
1 创建Django项目
django-admin startproject django_15

2 配置数据库
pip install mysqlclient
django_15/__init__.py   import mysqlclient
django_15/settings.py    修改DATABASES
数据库中创建数据库     create database django_15

3 创建app并载入Settings
django-admin startapp goods
将goods写入django_15/settings.py  INSTALLED_APPS

4 配置时区与静态文件夹

5 定义模型类
APP/models.py

6 数据迁移
python manage.py makemigrations
python manage.py migrate

7 创建测试数据
复制一份manage.py 为 build_models.py, 加入内容，然后运行

8 Admin注册模型类   app/admin.py 中加入以下内容
@admin.register(被注册的模型类名)
class 类名任意(admin.ModelAdmin):
    pass

9 创建超级管理员
python manage.py createsuperuser

10 登录后台管理
python manage.py runserver 8002
http://127.0.0.1:8002/admin/     可登录访问



Admin首页定制
11 app名字与表名配置
goods/app.py：
from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'goods'
    # 加入
    verbose_name = '商品管理'


goods/models.py:
from django.db import models


import datetime

class Category(models.Model):
    name = models.CharField(max_length=32)
    pcategory = models.ForeignKey('self',null=True,on_delete=models.CASCADE)
    path = models.URLField(max_length=255)
    createDatetime = models.DateTimeField(default=datetime.datetime.now())
    # 加入
    class Meta():
        verbose_name = verbose_name_plural = '商品分类'


12 header和title配置
在任意一个admin.py中加入
admin.site.site_header = 'XXX公司后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'



字段显示配置
13 展示与过滤     app/admin.py 中加入以下内容
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

     list_display = ['account','name','img','gender','tel','email','state','createDatetime']
     list_filter = ['state','gender','createDatetime']
     search_fields = ['account','name','tel']

14 配置字段的verbose_name    app/models.py
account = models.CharField(max_length=32,unique=True,verbose_name='账号')

15 choices设置    app/models.py
choice = (
	(【数据库中存储的值】，【显示的名称】),
	(【数据库中存储的值】，【显示的名称】),
)
gender = models.PositiveSmallIntegerField(default=0,verbose_name='性别',choices=choice)

16 配置增加页面
   app/admin.py  模型中增加 fieldsets


本项目具体参考: https://blog.csdn.net/kzl_knight/article/details/90441297
