# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-05-21 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch_buy', '0005_order_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Goods')),
            ],
            options={
                'verbose_name': '订单图书',
                'verbose_name_plural': '订单图书',
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='ISBN',
        ),
        migrations.AddField(
            model_name='order',
            name='qq',
            field=models.CharField(default=445, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='telephone',
            field=models.CharField(default=13807910737, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default=330049, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(default='liuziming', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordergood',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watch_buy.Order'),
        ),
    ]