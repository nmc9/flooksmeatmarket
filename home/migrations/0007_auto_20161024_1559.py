# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_basket_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='Date',
            field=models.DateField(blank=True),
        ),
    ]
