# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20160923_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='evenmore',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='product',
            name='moreotherfeild',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='otherfeild',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
