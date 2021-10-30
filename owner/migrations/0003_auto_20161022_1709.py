# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_owner_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='OpenFrom',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='OpenUntil',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='hourEnd',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='hourStart',
        ),
        migrations.AddField(
            model_name='owner',
            name='OpenFromWD',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='OpenSaturday',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='owner',
            name='OpenSunday',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='owner',
            name='OpenUntilWD',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='SaturdayEnd',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='SaturdayStart',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='SundayEnd',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='SundayStart',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='WeekdayEnd',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='WeekdayStart',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
