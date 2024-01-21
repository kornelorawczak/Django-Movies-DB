
from django.contrib import admin
from django.urls import path

from MoviesDB_KO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movies_list),
    path('actors/', views.actors_list),
    path('directors/', views.directors_list),
    path('directors/<int:id>/', views.directors_detail),
    path('actors/<int:id>/', views.actors_detail),
    path('movies/<int:id>/', views.movies_detail),
    path('actors/<int:id>/movies/', views.actor_movies),
    path('directors/<int:id>/movies/', views.director_movies),
    path('directors/<str:director_name>/', views.director_by_name, name='director_by_name'),
    path('actors/<str:actor_name>/', views.actor_by_name, name='actor_by_name'),
]
