# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-18 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160318_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='presenca',
            name='nome',
            field=models.CharField(default=1, max_length=50, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
