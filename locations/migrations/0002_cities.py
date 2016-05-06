# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('postalcode', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=30)),
                ('county', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(max_digits=9, decimal_places=6)),
                ('longitude', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
        ),
    ]
