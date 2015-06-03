# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20150603_0642'), # I changed the number so this 
                                             # auto-generated migration would be
                                             # after the custom one.
        ('tires', '0001_initial'), # Make certain the tires db state is setup
    ]

    # This migration was auto-generated when I changed the model FK references.
    # We need to remove the DeleteModel operation because that model exists in 
    # state only. 
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
        # Cut the DeleteModel operation. Will use in next migration.
    ]
