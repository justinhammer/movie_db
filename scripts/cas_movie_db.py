#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()


from main.models import Movie, MovieCas

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd_csv.txt"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    dvd_name = unidecode(row['DVD_Title'])

    print dvd_name

    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('dvdjango')
    movie = MovieCas(title=dvd_name)
    movie.save()

    cluster.shutdown()
