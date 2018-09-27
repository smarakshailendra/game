# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-27 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('method_type', models.CharField(db_index=True, max_length=255)),
                ('header', models.TextField(default='')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('path', models.CharField(blank=True, max_length=256, null=True)),
                ('query', models.CharField(blank=True, max_length=256, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'process',
            },
        ),
    ]