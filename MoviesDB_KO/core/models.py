from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Directors(models.Model): 
    # Django model that represents movie directors, it is in an one to many relationship with Movies model
    name = models.CharField(max_length=250) # Field that represents directors' full name and surname
    date_of_birth = models.DateField(null=True) # Field that represents director's date of birth in American YYYY-MM-DD format
    latest_movie = models.CharField(max_length=200, default=' ', null=True) # Field that represents directors' latest directed movie

    def __str__(self):
        return self.name


class Actors(models.Model): 
    # Django model that represents actors, it is in an one to many relationship with Movies model
    name = models.CharField(max_length=250) # Field that represents actors' full name and surname
    date_of_birth = models.DateField(null=True) # Field that represents actors' date of birth in an American YYYY-MM-DD format
    latest_movie = models.CharField(max_length=200, default=' ', null=True) # Field that represents actors' latest movie he starred in

    def __str__(self):
        return self.name


class Movies(models.Model):  
    # Django model that represents movies, it is in an many to one relation with both Directors and Actors model
    title = models.CharField(max_length=100) # Field that represents title of the movie
    premiere_date = models.DateField(null=True, default=None) # Field that represents premiere date of the movie, in an American YYYY-MM-DD format
    director = models.ForeignKey(Directors, on_delete=models.SET_NULL, related_name='movies', null=True, default=' ') # Field that represents an id of a director of this movie, it is a foreign key to the Directors model
    category = models.CharField(default=' ', max_length=200, null=True) # Field that specifies the category of a movie
    lead_actor = models.ForeignKey(Actors, on_delete=models.SET_NULL, related_name='movies', null=True, default=' ') # Field that represents an id of a lead actor of this movie, it is a foreign key to the Acotrs model
    academy_awards = models.SmallIntegerField( # Field that represents number of Academy Awards granted this movie
        validators=[MinValueValidator(0), MaxValueValidator(11)], default=None, null=True
    ) 

    def __str__(self):
        return self.title
