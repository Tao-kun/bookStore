# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-21 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_manage', '0004_user_money'),
        ('watch_buy', '0002_goods_intro_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderid', models.AutoField(primary_key=True, serialize=False)),
                ('orderdate', models.DateTimeField()),
                ('shipdate', models.DateTimeField()),
                ('address', models.CharField(max_length=255)),
                ('IsShipped', models.IntegerField(default=0)),
                ('IsCancle', models.IntegerField(default=0)),
                ('IsHandled', models.IntegerField(default=0)),
                ('IsCancled', models.IntegerField(default=0)),
                ('count', models.IntegerField()),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_manage.User')),
            ],
        ),
    ]
