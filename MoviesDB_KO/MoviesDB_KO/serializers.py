from rest_framework import serializers
from core.models import Movies, Actors, Directors

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'premiere_date', 'director', 'category', 'lead_actor', 'academy_awards']

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['id', 'name', 'date_of_birth', 'latest_movie']

class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = ['id', 'name', 'date_of_birth', 'latest_movie']