from django.contrib import admin
from .models import MoviePoster, Rating,Actor
# Register your models here.

admin.site.register(MoviePoster)
admin.site.register(Rating)
admin.site.register(Actor)