# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-03 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0010_auto_20170602_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name'], 'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0430\u043b\u0435\u0440\u0435\u044f', 'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0430\u043b\u0435\u0440\u0435\u0457'},
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='image/fotogalery/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f'),
        ),
    ]
