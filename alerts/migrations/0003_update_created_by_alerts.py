# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_add_created_by_alerts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
