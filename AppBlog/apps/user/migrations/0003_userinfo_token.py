# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190503_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
