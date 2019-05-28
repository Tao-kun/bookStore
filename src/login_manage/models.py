from django.db import models


class User(models.Model):
    studentID = models.CharField(max_length=255, primary_key=True, unique=True, verbose_name='学号')
    name = models.CharField(max_length=255, unique=True, verbose_name='姓名')
    password = models.CharField(max_length=255, verbose_name='密码')
    email = models.EmailField(max_length=255, verbose_name='邮箱地址')
    city = models.CharField(max_length=20, null=True, verbose_name='城市')  # 在select下拉菜单中的值，也就是城市的value
    city_num = models.IntegerField(null=True, verbose_name='城市编号')  # 在select下拉菜单中的编号
    detail_address = models.CharField(max_length=255, null=True, verbose_name='详细地址')
    zip_code = models.CharField(max_length=20, null=True, verbose_name='邮编')
    telephone = models.CharField(max_length=20, null=True, verbose_name='电话')
    qq = models.CharField(max_length=20, null=True, verbose_name='QQ号')
    money = models.FloatField(null=True, verbose_name='账户余额')
    is_banned = models.IntegerField(default=0, verbose_name='账户状态')

    def __str__(self):
        return '{}({})'.format(self.name, self.studentID)

    class Meta:
        verbose_name = "普通用户"
        verbose_name_plural = verbose_name
