# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0002_auto_20170530_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='buy',
            new_name='sell',
        ),
    ]
