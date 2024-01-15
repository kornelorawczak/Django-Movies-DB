"""
URL configuration for MoviesDB_KO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
