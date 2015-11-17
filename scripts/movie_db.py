#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Movie, MovieCas, Genre, Studio

import django
django.setup()

#cassandra imports
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd_csv.txt"

dvd_csv = os.path.join(dir_name, file_name)

csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('dvdjango4')

for row in reader:
    new_genre, created = Genre.objects.get_or_create(genre=row['Genre'])
    new_studio, created = Studio.objects.get_or_create(studio=row['Studio'])

    new_movie, created = Movie.objects.get_or_create(dvd_title=unidecode(row['DVD_Title']))
    new_movie.status = row['Status']
    new_movie.price = row['Price']
    new_movie.rating = row['Rating']
    new_movie.dvd_release_date = row['DVD_ReleaseDate']

    new_movie.genre = new_genre
    new_movie.studio = new_studio

    try:
            new_movie.save()
    except:
        print "nope"

    dvd_name = unidecode(row['DVD_Title'])

    if new_movie.id != None:
        new_movie_id = new_movie.id
    else:
        new_movie_id = 10
 
    movie = MovieCas(title=dvd_name, sql_id=new_movie_id)
    movie.save()

cluster.shutdown()
