# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Affiliate',
                'verbose_name_plural': 'Affiliates',
            },
        ),
        migrations.DeleteModel(
            name='Affilate',
        ),
    ]
