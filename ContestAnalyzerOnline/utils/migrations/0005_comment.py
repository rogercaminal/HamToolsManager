# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-15 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ContestAnalyzerOnline', '0004_delete_contestinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=10000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
