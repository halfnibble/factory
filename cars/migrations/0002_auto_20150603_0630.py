# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='tires',
            field=models.ForeignKey(to='tires.Tires'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(default=2015, verbose_name=b'Year'),
        ),
        migrations.DeleteModel(
            name='Tires',
        ),
    ]
