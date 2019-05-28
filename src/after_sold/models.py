from django.db import models

from login_manage.models import User
from watch_buy.models import Goods


class Comment(models.Model):
    content = models.TextField(null=False, verbose_name='评论内容')  # 用户发表评论后不可修改！
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='用户')
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, null=False, verbose_name='商品')
    quality = models.FloatField(null=False, verbose_name='评分')
    c_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='评论发布时间')

    def __str__(self):
        return '{}-{}-{}...'.format(self.user.name, self.good.GoodName, self.content[:32])

    class Meta:
        verbose_name = "图书评论"
        verbose_name_plural = verbose_name
