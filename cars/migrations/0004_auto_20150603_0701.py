# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20150603_0630'),
    ]

    # This needs to be a state-only operation because the database model was
    # renamed, and no longer exists according to Django.
    state_operations = [
        # Pasted from auto-generated operations in previous step:
        migrations.DeleteModel(
            name='Tires',
        ),
    ]

    operations = [
        # After this state operation, the Django DB state should match the 
        # actual database structure.
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]


