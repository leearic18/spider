# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HightechInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='\u5e8f\u53f7')),
                ('KeyID', models.CharField(max_length=255, verbose_name='\u8bc1\u4e66\u7f16\u53f7')),
                ('Unit_name', models.CharField(max_length=255, verbose_name='\u5355\u4f4d\u540d\u79f0')),
                ('address', models.CharField(max_length=255, verbose_name='\u5730\u5740')),
                ('Subordinate_Domain', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u9886\u57df')),
                ('type', models.CharField(max_length=255, verbose_name='\u9ad8\u4f01\u7c7b\u522b')),
            ],
        ),
    ]