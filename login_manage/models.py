from django.db import models

# Create your models here.

# 用户数据表，有
# 1.学号
# 2.姓名
# 3.密码
# 4.email   字段


class User(models.Model):
    studentID = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return str(self.studentID)

    class Meta:
        verbose_name = "普通用户"
        verbose_name_plural = verbose_name

