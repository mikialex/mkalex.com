# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='page_view',
            field=models.IntegerField(default=0),
        ),
    ]
