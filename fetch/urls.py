from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movies[/]?$', views.GetMovies.as_view(), name='home'),
]