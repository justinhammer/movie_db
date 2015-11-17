# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dvd_title', models.CharField(max_length=255, null=True, blank=True)),
                ('studio', models.CharField(max_length=255, null=True, blank=True)),
                ('released', models.CharField(max_length=30, null=True, blank=True)),
                ('status', models.CharField(max_length=30, null=True, blank=True)),
                ('sound', models.CharField(max_length=30, null=True, blank=True)),
                ('versions', models.CharField(max_length=30, null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('rating', models.CharField(max_length=10, null=True, blank=True)),
                ('year', models.CharField(max_length=10, null=True, blank=True)),
                ('Genre', models.CharField(max_length=100, null=True, blank=True)),
                ('aspect', models.CharField(max_length=10, null=True, blank=True)),
                ('upc', models.IntegerField(null=True, blank=True)),
                ('dvd_release_date', models.DateTimeField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
