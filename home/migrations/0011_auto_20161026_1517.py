# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20161025_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Beef', 'Beef'), ('Poultry', 'Poultry'), ('Pork', 'Pork'), ('Deli', 'Deli'), ('Specialty Meats', 'Specialty Meats'), ('Groceries', 'Groceries')], default='Groceries', max_length=20),
        ),
    ]
