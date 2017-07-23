# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20170723_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.IntegerField(choices=[(0, '待确认'), (1, '已确认'), (-1, '无效')], default=0, verbose_name='状态'),
        ),
    ]