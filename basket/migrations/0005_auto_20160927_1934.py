# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_auto_20160923_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.Basket'),
        ),
    ]