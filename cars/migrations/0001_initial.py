# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Car Model')),
                ('year', models.IntegerField(default=2015, max_length=4, verbose_name=b'Year')),
                ('color', models.CharField(default=b'White', max_length=20, verbose_name=b'Color')),
            ],
        ),
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Brand Name')),
                ('size', models.FloatField(default=17.0, verbose_name=b'Tire R')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='tires',
            field=models.ForeignKey(to='cars.Tires'),
        ),
    ]
