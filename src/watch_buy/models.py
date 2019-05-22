from django.db import models
from login_manage.models import User
# Create your models here.


# 商品信息
# 期中Intro_pic为这个商品详细页面的那个长的解释图
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
    Intro_pic = models.ImageField(null=True)

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name


# 商品所有的描述图片
class GoodsPic(models.Model):
    PicId = models.AutoField(primary_key=True)
    GoodISBN = models.ForeignKey(Goods, to_field='GoodISBN')
    GoodPic = models.ImageField()

    class Meta:
        verbose_name = "商品图像"
        verbose_name_plural = verbose_name


# 购物车记录
class Cart(models.Model):
    studentID = models.ForeignKey(User, to_field='studentID')
    GoodID = models.ForeignKey(Goods, to_field='GoodISBN')
    Qty = models.IntegerField(default=1)

    class Meta:
        verbose_name = "购物车信息"
        verbose_name_plural = verbose_name


# 订单
class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    orderdate = models.DateTimeField()
    shipdate = models.DateTimeField(null=True)  # 是否发货，由管理员决定
    user = models.ForeignKey(User, to_field="studentID")
    address = models.CharField(max_length=255)
    IsShipped = models.IntegerField(default=0)
    IsCancle = models.IntegerField(default=0)
    IsHandled = models.IntegerField(default=0)
    IsCancled = models.IntegerField(default=0)
    username = models.CharField(max_length=20)
    telephone = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=25)
    qq = models.CharField(max_length=15)

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name


# 订单图书信息(因为一次订单可以订很多本书)
class OrderGood(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, to_field="orderid")
    good = models.ForeignKey(Goods, to_field="GoodISBN")
    count = models.IntegerField(default=1)

    class Meta:
        verbose_name = "订单图书"
        verbose_name_plural = verbose_name
