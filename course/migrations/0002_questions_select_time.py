# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-08 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='select_time',
            field=models.IntegerField(default=0, verbose_name='\u9009\u4e2d\u6b21\u6570'),
        ),
    ]
