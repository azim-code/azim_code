from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse as api_reverse
# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movies(models.Model):

    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100,null=True)
    genre = models.ManyToManyField(Genre)
    # genre = models.CharField(max_length=100)
    popularity = models.FloatField(null=True)
    imdb_score = models.FloatField(null=True)


    def __str__(self):
        return self.name

