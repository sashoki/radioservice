# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-05 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0018_auto_20170605_0932'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
    ]
