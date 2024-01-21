from core.models import Actors, Directors, Movies
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from MoviesDB_KO import serializers


@api_view(['GET', 'POST'])
def movies_list(request):
    # This api view allows to get data about all movies and add a new record to the movies table
    if request.method == 'GET':
        movies = Movies.objects.all()
        serializer = serializers.MoviesSerializer(movies, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTs)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, id):
    # This api view allows to get data about a specific movie, specified by its id and allows to update its data as well as delete the record
    try:
        movie = Movies.objects.get(pk=id)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.MoviesSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.MoviesSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def actors_list(request):
    # This api view allows to get data about all actors and add a new record to the actors table
    if request.method == 'GET':
        actors = Actors.objects.all()
        serializer = serializers.ActorsSerializer(actors, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.ActorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTs)


@api_view(['GET', 'PUT', 'DELETE'])
def actors_detail(request, id):
    # This api view allows to get data about a specific actors, specified by its id and allows to update its data as well as delete the record
    try:
        actor = Actors.objects.get(pk=id)
    except Actors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.ActorsSerializer(actor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.ActorsSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def actor_movies(request, id):
    # This api view allows to get data about all the movies that selected (by an id) actor starred in
    actor = get_object_or_404(Actors, pk=id)
    movies = Movies.objects.filter(lead_actor=actor)
    serializer = serializers.MoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_by_name(request, actor_name):
    # This api view allows to get information about specified actor by his name
    actor = get_object_or_404(Actors, name__iexact=actor_name)
    serializer = serializers.ActorsSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def director_movies(request, id):
    # This api view allows to get data about all the movies that selected (by an id) director directed
    director = get_object_or_404(Directors, pk=id)
    movies = Movies.objects.filter(director=director)
    serializer = serializers.MoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_by_name(request, director_name):
    # This api view allows to get information about specified director by his name
    director = get_object_or_404(Directors, name__iexact=director_name)
    serializer = serializers.DirectorsSerializer(director)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def directors_list(request):
    # This api view allows to get data about all directors and add a new record to the directors table
    if request.method == 'GET':
        directors = Directors.objects.all()
        serializer = serializers.DirectorsSerializer(directors, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = serializers.DirectorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTs)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail(request, id):
    # This api view allows to get data about a specific director, specified by its id and allows to update its data as well as delete the record
    try:
        director = Directors.objects.get(pk=id)
    except Directors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = serializers.DirectorsSerializer(director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DirectorsSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
