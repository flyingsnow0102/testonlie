# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-19 05:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_auto_20180416_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_time', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('pub_content', models.TextField(verbose_name='\u901a\u77e5\u8be6\u60c5')),
                ('pub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u53d1\u5e03\u4eba')),
            ],
            options={
                'verbose_name': '\u901a\u77e5\u53d1\u5e03',
                'verbose_name_plural': '\u901a\u77e5\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='UserAnswerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='\u7528\u6237\u7b54\u6848')),
                ('score', models.CharField(default=0, max_length=100, verbose_name='\u5206\u6570')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u4f5c\u7b54\u65f6\u95f4')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='\u8bfe\u7a0b')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Paper', verbose_name='\u8bd5\u5377')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Questions', verbose_name='\u9898\u76ee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u505a\u9898\u8bb0\u5f55',
                'verbose_name_plural': '\u7528\u6237\u505a\u9898\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='UserNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u7559\u8a00\u65f6\u95f4')),
                ('note_content', models.TextField(default='', verbose_name='\u7559\u8a00\u5185\u5bb9')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7559\u8a00\u4eba')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7559\u8a00',
                'verbose_name_plural': '\u7528\u6237\u7559\u8a00',
            },
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0, verbose_name='\u603b\u5206')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='\u5f55\u5165\u65f6\u95f4')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.PaperList', verbose_name='\u8bd5\u5377')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u603b\u5206',
                'verbose_name_plural': '\u7528\u6237\u603b\u5206',
            },
        ),
    ]
