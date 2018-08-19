# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180211_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosisinfo',
            name='Constipation',
        ),
        migrations.AddField(
            model_name='diagnosisinfo',
            name='Stomach_Pain',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=10, null=True),
        ),
    ]
