# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20160927_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.Basket'),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(choices=[('Fridge', 'Fridge'), ('Rack', 'Rack'), ('Ask', 'Ask')], default='ASK', max_length=20),
        ),
    ]
