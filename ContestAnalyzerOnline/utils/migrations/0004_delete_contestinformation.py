# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-21 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContestAnalyzerOnline', '0003_auto_20170921_1601'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContestInformation',
        ),
    ]
