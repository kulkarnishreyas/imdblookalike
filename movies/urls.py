from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('search_movies', views.search, name='movies-search'),
    path('create', views.create, name='create')
]