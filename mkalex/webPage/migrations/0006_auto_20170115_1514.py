# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0005_auto_20170115_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
