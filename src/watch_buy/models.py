from django.db import models

from login_manage.models import User


class Goods(models.Model):
    """
    商品信息
    其中Intro_pic为这个商品详细页面的那个长的解释图
    """
    GoodISBN = models.CharField(max_length=50, primary_key=True, verbose_name='ISBN')
    GoodName = models.CharField(max_length=255, unique=True, verbose_name='书籍名称')
    GoodPrice = models.FloatField(verbose_name='单价')
    GoodAuthor = models.CharField(max_length=255, null=True, blank=True, verbose_name='作者')
    GoodIntro = models.TextField(null=True, blank=True, verbose_name='商品介绍')
    GoodRemain = models.IntegerField(default=0, verbose_name='库存')
    GoodDiscount = models.FloatField(default=1.0, verbose_name='折扣')
    IsForSale = models.IntegerField(default=0, verbose_name='是否打折')
    IsNew = models.IntegerField(default=0, verbose_name='是否新品')
    Intro_pic = models.ImageField(null=True, blank=True, verbose_name='介绍图片')
    Category = models.CharField(null=True, blank=True, max_length=20, verbose_name='分类')
    Publisher = models.CharField(null=True, max_length=100, verbose_name='出版社')
    Pages = models.IntegerField(null=True, verbose_name='页数')
    PublishDate = models.DateField(null=True, verbose_name='出版日期')
    PrintDate = models.DateField(null=True, verbose_name='印刷日期')
    Size = models.CharField(null=True,max_length=20, verbose_name='开本')
    Edition = models.IntegerField(null=True, verbose_name='版本')

    def __str__(self):
        return '{}({})'.format(self.GoodName, self.GoodISBN)

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name


#
class GoodsPic(models.Model):
    """商品所有的描述图片"""
    PicId = models.AutoField(primary_key=True, verbose_name='图片ID')
    GoodISBN = models.ForeignKey(Goods, to_field='GoodISBN', verbose_name='图书信息')
    GoodPic = models.ImageField(verbose_name='文件名')

    def __str__(self):
        return '{}({})'.format(self.GoodISBN.GoodName, self.GoodPic)

    class Meta:
        verbose_name = "商品图像"
        verbose_name_plural = verbose_name


class Cart(models.Model):
    """购物车记录"""
    studentID = models.ForeignKey(User, to_field='studentID', verbose_name='学号')
    GoodID = models.ForeignKey(Goods, to_field='GoodISBN', verbose_name='商品信息')
    Qty = models.IntegerField(default=1, verbose_name='数量')

    def __str__(self):
        return "{}-{}".format(self.studentID.name, self.GoodID.GoodName)

    class Meta:
        verbose_name = "购物车信息"
        verbose_name_plural = verbose_name


class Order(models.Model):
    """订单"""
    orderid = models.AutoField(primary_key=True, verbose_name='订单号')
    orderdate = models.DateTimeField(verbose_name='下单时间')
    shipdate = models.DateTimeField(null=True, blank=True, verbose_name='发货时间')
    user = models.ForeignKey(User, to_field="studentID", verbose_name='下单用户')
    address = models.CharField(max_length=255, verbose_name='收货人地址')
    IsShipped = models.IntegerField(default=0, verbose_name='是否发货')
    IsCancle = models.IntegerField(default=0, verbose_name='是否取消订单')
    IsHandled = models.IntegerField(default=0, verbose_name='是否确认订单')
    IsCancled = models.IntegerField(default=0, verbose_name='是否完成退款')
    username = models.CharField(max_length=20, verbose_name='收货人姓名')
    telephone = models.CharField(max_length=25, verbose_name='收货人电话')
    zipcode = models.CharField(max_length=25, verbose_name='收货人邮编')
    qq = models.CharField(max_length=15, null=True, blank=True, verbose_name='收货人QQ')
    IsCompleted = models.IntegerField(default=0, verbose_name='订单是否完成')
    Comment = models.CharField(max_length=500, null=True, blank=True, verbose_name='用户评论')
    IsReturn = models.IntegerField(default=0, verbose_name='是否退回')

    def __str__(self):
        return '{}-{}({})'.format(self.orderid, self.user.name, self.orderdate)

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name


class OrderGood(models.Model):
    """订单图书信息(因为一次订单可以订很多本书)"""
    id = models.AutoField(primary_key=True, verbose_name='订单号')
    order = models.ForeignKey(Order, to_field="orderid", verbose_name='订单信息')
    good = models.ForeignKey(Goods, to_field="GoodISBN", verbose_name='商品信息')
    count = models.IntegerField(default=1, verbose_name='数量')

    def __str__(self):
        return '{}({})'.format(self.good.GoodName, self.id)

    class Meta:
        verbose_name = "订单图书"
        verbose_name_plural = verbose_name
