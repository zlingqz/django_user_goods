from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = 'XXX公司后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'
