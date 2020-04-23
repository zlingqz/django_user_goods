from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)
    pcategory = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    path = models.URLField(max_length=255)
    createDatetime = models.DateTimeField(default=datetime.datetime.now())

    class Meta():
        verbose_name = verbose_name_plural = '商品分类'
