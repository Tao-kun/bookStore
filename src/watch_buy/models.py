from django.db import models
from login_manage.models import User
# Create your models here.


#  商品信息
class Goods(models.Model):
    GoodISBN = models.CharField(max_length=50, primary_key=True)
    GoodName = models.CharField(max_length=255, unique=True)
    GoodPrice = models.FloatField()
    GoodAuthor = models.CharField(max_length=255, null=True)
    GoodIntro = models.TextField(null=True)
    GoodRemain = models.IntegerField(default=0)
    GoodDiscount = models.FloatField(default=1.0)
    IsForSale = models.IntegerField(default=0)
    IsNew = models.IntegerField(default=0)

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name


class GoodsPic(models.Model):
    PicId = models.AutoField(primary_key=True)
    GoodISBN = models.ForeignKey(Goods, to_field='GoodISBN')
    GoodPic = models.ImageField()

    class Meta:
        verbose_name = "商品图像"
        verbose_name_plural = verbose_name


#  购物车
class Cart(models.Model):
    studentID = models.ForeignKey(User, to_field='studentID')
    GoodID = models.ForeignKey(Goods, to_field='GoodISBN')
    Qty = models.IntegerField(default=1)

    class Meta:
        verbose_name = "购物车信息"
        verbose_name_plural = verbose_name
