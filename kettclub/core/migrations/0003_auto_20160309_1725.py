# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-09 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160309_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atleta',
            old_name='saudeanamnese',
            new_name='id_saudeanamnese',
        ),
        migrations.AddField(
            model_name='saudeanamnese',
            name='id_atleta',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Atleta'),
            preserve_default=False,
        ),
    ]