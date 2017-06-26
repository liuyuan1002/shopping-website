# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taobao', '0004_goods_goods_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('total', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantuty', models.IntegerField(default=1)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goods_id', models.CharField(max_length=10)),
                ('cart_id', models.IntegerField(default=0)),
            ],
        ),
    ]
