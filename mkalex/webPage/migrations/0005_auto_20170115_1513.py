# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0004_auto_20170115_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='webPage.Tag'),
        ),
    ]
