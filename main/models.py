from django.db import models

#cassandra imports
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# Create your models here.


class Movie(models.Model):
    dvd_title = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    dvd_release_date = models.DateTimeField(null=True, blank=True)
    genre = models.ForeignKey('main.Genre', null=True, blank=True)
    studio = models.ForeignKey('main.Studio', null=True, blank=True)

    def __unicode__(self):
        return self.dvd_title


class MovieCas(Model):
    sql_id = columns.Integer(primary_key=True, required=False)
    title = columns.Text(required=False)
    uu_id = columns.UUID(primary_key=True, default=uuid.uuid4)


class Genre(models.Model):
    genre = models.CharField(max_length=100, null=True, blank=True)


class Studio(models.Model):
    studio = models.CharField(max_length=255, null=True, blank=True)