# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-15 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContestAnalyzerOnline', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
