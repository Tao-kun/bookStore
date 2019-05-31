# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0004_auto_20190530_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='Edition',
            field=models.IntegerField(null=True, verbose_name='版本'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Pages',
            field=models.IntegerField(null=True, verbose_name='页数'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='PrintDate',
            field=models.DateField(null=True, verbose_name='印刷日期'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='PublishDate',
            field=models.DateField(null=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Publisher',
            field=models.CharField(max_length=100, null=True, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Size',
            field=models.CharField(max_length=20, null=True, verbose_name='开本'),
        ),
    ]
