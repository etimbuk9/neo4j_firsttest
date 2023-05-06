from django.contrib import admin as dj_admin
from django_neomodel import admin as neoadmin
from .models import Movie

# Register your models here.

class MovieAdmin(dj_admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ['title']

neoadmin.register(Movie, MovieAdmin)