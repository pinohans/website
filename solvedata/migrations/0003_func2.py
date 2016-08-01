# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 07:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solvedata', '0002_auto_20160801_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Func2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('func2', 'Can use func2'),),
            },
        ),
    ]
