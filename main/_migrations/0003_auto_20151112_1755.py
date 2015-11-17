# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151112_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='aspect',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='released',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='sound',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='upc',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='versions',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
