# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-18 10:14
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u043e\u0432\u0438\u043d\u0438')),
                ('news_text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430 \u0447\u0430\u0441\u0442\u0438\u043d\u0430')),
                ('news_date', models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0456\u043a\u0430\u0446\u0456\u0457')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='\u0412\u0456\u0434\u0435\u043e')),
            ],
            options={
                'db_table': 'News',
                'verbose_name': '\u041d\u043e\u0432\u0438\u043d\u0438 \u0444\u0456\u0440\u043c\u0438',
                'verbose_name_plural': '\u041d\u043e\u0432\u0438\u043d\u0438 \u0444\u0456\u0440\u043c\u0438',
            },
        ),
    ]
