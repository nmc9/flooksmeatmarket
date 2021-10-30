# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=7),
        ),
    ]