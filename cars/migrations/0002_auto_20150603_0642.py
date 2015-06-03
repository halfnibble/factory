# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'), # Change dependency to NOT use last auto-migration
    ]

    # Add custom database_operations
    database_operations = [
        # You have to use Django's database table naming defaults to get the 
        # name 'tires_tires'. It is basically <app_name>_<model_name>.
        migrations.AlterModelTable('tires', 'tires_tires'),  
    ]

    # Don't modify the Django 'state' yet
    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
