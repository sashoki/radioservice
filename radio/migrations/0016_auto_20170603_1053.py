# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-03 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0015_auto_20170603_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0444\u043e\u0442\u043e\u0433\u0430\u043b\u0435\u0440\u0435\u0457'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
    ]