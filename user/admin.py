from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.shortcuts import reverse
from hashlib import md5

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ['account', 'name', 'show_img', 'gender', 'tel', 'email', 'state', 'createDatetime', 'operator']
   list_filter = ['state', 'gender', 'createDatetime']
   search_fields = ['account', 'name', 'tel']

   def show_img(self,obj):
      src = '/static/%s' % obj.img
      html = '<a herf="%s"><img style="width:20px; height:20px;" src="%s"></a>' % (src, src)
      return format_html(html)

   show_img.short_description = '头像'

   def operator(self, obj):
      change_href = reverse('admin:user_user_change', args=(obj.id,))
      delete_href = reverse('admin:user_user_delete', args=(obj.id,))
      html = '<a style="color:deepskyblue;" href="%s">编辑</a>&#12288;<a style="color:palevioletred;" href="%s">删除</a>'\
             % (change_href, delete_href)
      return format_html(html)
   operator.short_description = '操作'

   def save_model(self, request, obj, form, change):
      if not obj.id:
         obj.password = md5(obj.password.encode('utf-8')).hexdigest()
      elif User.objects.get(id=obj.id).password != obj.password:
         obj.password = md5(obj.password.encode('utf-8')).hexdigest()
      return super(UserAdmin, self).save_model(request, obj, form, change)

   fieldsets = [
      [
         '基础配置', {
         'fields': ['account', 'name', 'password', 'tel', 'email', 'gender'],
      }
      ],
      [
         '高级配置', {
         'fields': ['img', 'state', 'createDatetime'],
         'classes': ('collapse',)
      }
      ]
   ]
