# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('zip', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=27)),
                ('state', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('timezone', models.SmallIntegerField()),
                ('daylight_savings_time', models.BooleanField(default=True)),
            ],
        ),
    ]
