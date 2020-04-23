from django.db import models
import datetime, os, uuid

def uploadfile(instance,filename):
    suffix = filename.rsplit('.')[-1]
    filename_new = '%s.%s' % (uuid.uuid4().__str__(),suffix)
    filepath = os.path.join('img',filename_new)
    return filepath

# Create your models here.
class User(models.Model):
    GENDER_ITEM = ((0, '男'), (1, '女'))
    STATE_ITEM = ((1, '启用'), (2, '禁用'), (3, '后台管理员'))
    account = models.CharField(max_length=32, unique=True, verbose_name='账号')
    name = models.CharField(max_length=16, null=True, verbose_name='真实姓名')
    img = models.ImageField(upload_to=uploadfile, null=True, verbose_name='头像')
    password = models.CharField(max_length=32, verbose_name='密码')
    gender = models.PositiveSmallIntegerField(default=0, verbose_name='性别', choices=GENDER_ITEM)
    tel = models.CharField(max_length=11, null=True, verbose_name='手机号')
    email = models.EmailField(null=True, verbose_name='邮箱')
    state = models.PositiveSmallIntegerField(default=1, verbose_name='状态', choices=STATE_ITEM)
    createDatetime = models.DateTimeField(default=datetime.datetime.now(), verbose_name='创建时间')



    class Meta():
        verbose_name = verbose_name_plural = '用户信息'
