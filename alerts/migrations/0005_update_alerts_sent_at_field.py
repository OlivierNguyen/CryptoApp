# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_update_alerts_operator_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='sent_at',
            field=models.DateField(null=True),
        ),
    ]
