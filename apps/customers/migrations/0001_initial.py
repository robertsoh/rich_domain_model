# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-21 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('status', models.IntegerField()),
                ('status_expiration_date', models.DateTimeField(blank=True, null=True)),
                ('money_spent', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
