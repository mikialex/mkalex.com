# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webPage', '0010_auto_20170115_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommended_article',
            name='article',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_recommended', to='webPage.Article'),
        ),
    ]
