# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-16 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContestAnalyzerOnline', '0008_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
