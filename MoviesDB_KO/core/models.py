from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Directors(models.Model):  # one to many with Movies
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)
    latest_movie = models.CharField(max_length=200, default=' ', null=True)

    def __str__(self):
        return self.name


class Actors(models.Model):  # one to many with Movies
    name = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)
    latest_movie = models.CharField(max_length=200, default=' ', null=True)

    def __str__(self):
        return self.name


class Movies(models.Model):  # many to one relation with Directors, Actors
    title = models.CharField(max_length=100)
    premiere_date = models.DateField(null=True, default=None)
    director = models.ForeignKey(Directors, on_delete=models.SET_NULL, related_name='movies', null=True, default=' ')
    category = models.CharField(default=' ', max_length=200, null=True)
    lead_actor = models.ForeignKey(Actors, on_delete=models.SET_NULL, related_name='movies', null=True, default=' ')
    academy_awards = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(11)], default=None, null=True
    )

    def __str__(self):
        return self.title
