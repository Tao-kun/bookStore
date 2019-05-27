from django.db import models
from login_manage.models import *
from watch_buy.models import *


# Create your models here.

class Comment(models.Model):
    content = models.TextField(null=False)  # 用户发表评论后不可修改！
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, null=False)
    quality = models.FloatField(null=False)
    c_time = models.DateTimeField(auto_now_add=True, editable=False)  # 评论创建时间

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = "图书评论"
        verbose_name_plural = verbose_name
