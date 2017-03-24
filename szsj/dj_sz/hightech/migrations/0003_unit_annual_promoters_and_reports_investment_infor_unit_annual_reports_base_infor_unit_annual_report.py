# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hightech', '0002_auto_20170223_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_annual_Promoters_and_reports_investment_Infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('Sponsor', models.CharField(max_length=255, verbose_name='\u53d1\u8d77\u4eba')),
                ('Time_of_subscription', models.CharField(max_length=255, verbose_name='\u8ba4\u7f34\u51fa\u8d44\u65f6\u95f4')),
                ('Subscribed_capital_contribution', models.CharField(max_length=255, verbose_name='\u8ba4\u7f34\u51fa\u8d44\u65b9\u5f0f')),
                ('Paid_in_capital_contribution', models.CharField(max_length=255, verbose_name='\u5b9e\u7f34\u51fa\u8d44\u989d\uff08\u4e07\u5143\uff09')),
                ('Investment_time', models.CharField(max_length=255, verbose_name='\u51fa\u8d44\u65f6\u95f4')),
                ('Investment_method', models.CharField(max_length=255, verbose_name='\u51fa\u8d44\u65b9\u5f0f')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_annual_reports_Base_Infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('Registration_number', models.CharField(max_length=255, verbose_name='\u6ce8\u518c\u53f7')),
                ('Business_state', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u7ecf\u8425\u72b6\u6001')),
                ('Enterprise_telephone', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u8054\u7cfb\u7535\u8bdd')),
                ('Email', models.CharField(max_length=255, verbose_name='\u7535\u5b50\u90ae\u7bb1')),
                ('Postcode', models.CharField(max_length=255, verbose_name='\u90ae\u653f\u7f16\u7801')),
                ('number_of_people_engaged', models.CharField(max_length=255, verbose_name='\u4ece\u4e1a\u4eba\u6570')),
                ('residence', models.CharField(max_length=255, verbose_name='\u4f4f\u6240')),
                ('transfer_of_shareholder_equity', models.CharField(max_length=255, verbose_name='\u6709\u9650\u8d23\u4efb\u516c\u53f8\u672c\u5e74\u5ea6\u662f\u5426\u53d1\u751f\u80a1\u4e1c\u80a1\u6743\u8f6c\u8ba9')),
                ('investment_information', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u662f\u5426\u6709\u6295\u8d44\u4fe1\u606f\u6216\u8d2d\u4e70\u5176\u4ed6\u516c\u53f8\u80a1\u6743')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_annual_reports_Website_Infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('Web_Type', models.CharField(max_length=255, verbose_name='\u7c7b\u578b')),
                ('Web_Name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('Web_Site', models.CharField(max_length=255, verbose_name='\u7f51\u5740')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Base_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('phone_nunber', models.CharField(max_length=255, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('email', models.CharField(max_length=255, verbose_name='\u90ae\u7bb1')),
                ('website', models.CharField(max_length=255, verbose_name='\u7f51\u5740')),
                ('address', models.CharField(max_length=255, verbose_name='\u5730\u5740')),
                ('code', models.CharField(max_length=255, verbose_name='\u7edf\u4e00\u793e\u4f1a\u4fe1\u7528\u4ee3\u7801')),
                ('Registration_number', models.CharField(max_length=255, verbose_name='\u6ce8\u518c\u53f7')),
                ('Organization_code', models.CharField(max_length=255, verbose_name='\u7ec4\u7ec7\u673a\u6784\u4ee3\u7801')),
                ('Operating_state', models.CharField(max_length=255, verbose_name='\u7ecf\u8425\u72b6\u6001')),
                ('Legal_representative', models.CharField(max_length=255, verbose_name='\u6cd5\u5b9a\u4ee3\u8868\u4eba')),
                ('registered_capital', models.CharField(max_length=255, verbose_name='\u6ce8\u518c\u8d44\u672c')),
                ('Company_type', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u7c7b\u578b')),
                ('date_of_establishment', models.CharField(max_length=255, verbose_name='\u6210\u7acb\u65e5\u671f')),
                ('Operating_period', models.CharField(max_length=255, verbose_name='\u8425\u4e1a\u671f\u9650')),
                ('registration_authority', models.CharField(max_length=255, verbose_name='\u767b\u8bb0\u673a\u5173')),
                ('Date_of_issue', models.CharField(max_length=255, verbose_name='\u53d1\u7167\u65e5\u671f')),
                ('company_size', models.CharField(max_length=255, verbose_name='\u516c\u53f8\u89c4\u6a21')),
                ('Subordinate_industry', models.CharField(max_length=255, verbose_name='\u6240\u5c5e\u884c\u4e1a')),
                ('English_name', models.CharField(max_length=255, verbose_name='\u82f1\u6587\u540d')),
                ('Name_used_Before', models.CharField(max_length=255, verbose_name='\u66fe\u7528\u540d')),
                ('Enterprise_address', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5730\u5740')),
                ('Business_scope', models.CharField(max_length=255, verbose_name='\u7ecf\u8425\u8303\u56f4')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Base_Info_Changed_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('Change_date', models.CharField(max_length=255, verbose_name='\u53d8\u66f4\u65e5\u671f')),
                ('Change_item', models.CharField(max_length=255, verbose_name='\u53d8\u66f4\u9879\u76ee')),
                ('Before_change', models.CharField(max_length=255, verbose_name='\u53d8\u66f4\u524d')),
                ('After_change', models.CharField(max_length=255, verbose_name='\u53d8\u66f4\u540e')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Base_Info_Shareholder_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_id', models.CharField(max_length=255, verbose_name='\u4f01\u4e1a\u5e8f\u53f7')),
                ('Shareholder', models.CharField(max_length=255, verbose_name='\u80a1\u4e1c')),
                ('Shareholding_ratio', models.CharField(max_length=255, verbose_name='\u6301\u80a1\u6bd4\u4f8b')),
                ('Subscribed_capital_contribution', models.CharField(max_length=255, verbose_name='\u8ba4\u7f34\u51fa\u8d44\u989d')),
                ('Subscription_Date', models.CharField(max_length=255, verbose_name='\u8ba4\u7f34\u51fa\u8d44\u65e5\u671f')),
                ('Shareholder_type', models.CharField(max_length=255, verbose_name='\u80a1\u4e1c\u7c7b\u578b')),
            ],
        ),
    ]