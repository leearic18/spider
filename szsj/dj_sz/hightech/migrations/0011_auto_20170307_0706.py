# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hightech', '0010_idc_base_info_qicq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idc_base_info',
            old_name='qicq',
            new_name='QQ',
        ),
    ]