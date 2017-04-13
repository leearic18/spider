# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='base_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u80a1\u7968\u4ee3\u7801')),
                ('Company_name', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u540d\u5b57')),
                ('daima', models.CharField(max_length=255, verbose_name='\u80a1\u7968\u4ee3\u7801')),
                ('quancheng', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u5168\u79f0')),
                ('englishname', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u82f1\u6587\u540d\u79f0')),
                ('cengyongming', models.CharField(max_length=255, verbose_name='\u66fe\u7528\u540d')),
                ('chengliriqi', models.CharField(max_length=255, verbose_name='\u6210\u7acb\u65e5\u671f')),
                ('suoshuhangye', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u884c\u4e1a')),
                ('suoshugannian', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u6982\u5ff5')),
                ('suoshudiyu', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u5730\u57df')),
                ('fadingdabiaoren', models.CharField(max_length=255, verbose_name='\u6cd5\u5b9a\u4ee3\u8868\u4eba')),
                ('dulidongshi', models.CharField(max_length=255, verbose_name='\u72ec\u7acb\u8463\u4e8b')),
                ('zixunfuwujigou', models.CharField(max_length=255, verbose_name='\u54a8\u8be2\u670d\u52a1\u673a\u6784')),
                ('kuaijishiwusuo', models.CharField(max_length=255, verbose_name='\u4f1a\u8ba1\u5e08\u4e8b\u52a1\u6240')),
                ('zhengquanshifudaibiao', models.CharField(max_length=255, verbose_name='\u8bc1\u5238\u4e8b\u52a1\u4ee3\u8868')),
                ('faxingriqi', models.CharField(max_length=255, verbose_name='\u53d1\u884c\u65e5\u671f')),
                ('shangshiriqi', models.CharField(max_length=255, verbose_name='\u4e0a\u5e02\u65e5\u671f')),
                ('shangshijiaoyisuo', models.CharField(max_length=255, verbose_name='\u4e0a\u5e02\u4ea4\u6613\u6240')),
                ('zhengquanleixing', models.CharField(max_length=255, verbose_name='\u8bc1\u5238\u7c7b\u578b')),
                ('liutongguben', models.CharField(max_length=255, verbose_name='\u6d41\u901a\u80a1\u672c')),
                ('zongguben', models.CharField(max_length=255, verbose_name='\u603b\u80a1\u672c')),
                ('zhuchengxiaoshang', models.CharField(max_length=255, verbose_name='\u4e3b\u627f\u9500\u5546')),
                ('faxingjia', models.CharField(max_length=255, verbose_name='\u53d1\u884c\u4ef7')),
                ('shangshisourikaipanjia', models.CharField(max_length=255, verbose_name='\u4e0a\u5e02\u9996\u65e5\u5f00\u76d8\u4ef7')),
                ('shangshishourizhangdiefu', models.CharField(max_length=255, verbose_name='\u4e0a\u5e02\u9996\u65e5\u6da8\u8dcc\u5e45')),
                ('shangshishourihuanshoulv', models.CharField(max_length=255, verbose_name=' \u4e0a\u5e02\u9996\u65e5\u6362\u624b\u7387')),
                ('tebiechulihetuishi', models.CharField(max_length=255, verbose_name='\u7279\u522b\u5904\u7406\u548c\u9000\u5e02')),
                ('faxingshiyinglv', models.CharField(max_length=255, verbose_name='\u53d1\u884c\u5e02\u76c8\u7387')),
                ('zuixinshiyinglv', models.CharField(max_length=255, verbose_name='\u6700\u65b0\u5e02\u76c8\u7387')),
                ('zhuceziben', models.CharField(max_length=255, verbose_name='\u6ce8\u518c\u8d44\u672c')),
                ('zhucedizhi', models.CharField(max_length=255, verbose_name='\u6ce8\u518c\u5730\u5740')),
                ('suodeisuilv', models.CharField(max_length=255, verbose_name='\u6240\u5f97\u7a0e\u7387')),
                ('bangongdizhi', models.CharField(max_length=255, verbose_name='\u529e\u516c\u5730\u5740')),
                ('zhuyaochanpin', models.CharField(max_length=255, verbose_name='\u4e3b\u8981\u4ea7\u54c1(\u4e1a\u52a1)')),
                ('lianxidianhua', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u7535\u8bdd(\u8463\u79d8)')),
                ('gongsichuanzhen', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u4f20\u771f')),
                ('dianziyouxiang', models.CharField(max_length=255, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('gongsiwangzhi', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u7f51\u5740')),
                ('lianxiren', models.CharField(max_length=255, verbose_name='\u8054\u7cfb\u4eba')),
                ('youzhengbianma', models.CharField(max_length=255, verbose_name='\u90ae\u653f\u7f16\u7801')),
                ('jingyingfanwei', models.CharField(max_length=999, verbose_name='\u7ecf\u8425\u8303\u56f4')),
                ('gongsijianjie', models.CharField(max_length=999, verbose_name='\u516c\u53f8\u7b80\u4ecb')),
            ],
        ),
        migrations.CreateModel(
            name='Companys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=255, verbose_name='\u80a1\u7968\u4ee3\u7801')),
                ('Name', models.CharField(max_length=255, verbose_name='\u80a1\u7968\u7b80\u79f0')),
                ('ALl_Name', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u5168\u79f0')),
                ('History_Name', models.CharField(max_length=255, verbose_name='\u66fe\u7528\u540d')),
            ],
        ),
        migrations.CreateModel(
            name='Fenhong_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=255, verbose_name='\u516c\u544a\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Gaoguan_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u540d\u5b57')),
            ],
        ),
    ]