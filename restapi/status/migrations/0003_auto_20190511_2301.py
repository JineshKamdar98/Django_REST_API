# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-11 17:31
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20190503_2148'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='status',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
