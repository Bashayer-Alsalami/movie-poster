from django.shortcuts import render
from django.http import HttpResponse
from .models import MoviePoster
# Create your views here.

# class Coin:
#   def __init__ (self, name, year, duration, actors, color):
#     self.name = name
#     self.year = year
#     self.duration = duration
#     self.actors = actors
#     self.color = color

# coins = [
#   Coin('50th', 'clean', 100, 'russian', 'gold'),
#   Coin('60th', 'damaged', 10, 'American', 'silver'),
#   Coin('70th', 'whizzed', 25, 'saudi', 'rosegold'),
#   Coin('20th', 'need polishing', 50, 'unknown', 'gold')
# ]

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def movieposter_index(request):
  moviePosters = MoviePoster.objects.all()
  return render(request, 'movieposter/index.html', {'moviePosters': moviePosters})