# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Brand Name')),
                ('size', models.FloatField(default=17.0, verbose_name=b'Tire R')),
            ],
            options={
                'verbose_name_plural': 'Tires',
            },
        ),
    ]
