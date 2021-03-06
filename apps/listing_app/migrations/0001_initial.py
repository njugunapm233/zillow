# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0003_auto_20170530_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=5)),
                ('neighborhood', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('beds', models.SmallIntegerField()),
                ('baths', models.DecimalField(decimal_places=1, max_digits=5)),
                ('buy', models.BooleanField()),
                ('rent', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorites', models.ManyToManyField(related_name='favorites', to='user_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='user_app.User')),
            ],
        ),
    ]
