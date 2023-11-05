from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MoviePoster
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .forms import RatingForm
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
class MoviePosterCreate(CreateView):
  model = MoviePoster
  fields = ['name', 'year', 'duration', 'description', 'actors', 'image']

class MoviePosterUpdate(UpdateView):
  model = MoviePoster
  fields = ['name', 'year', 'duration', 'description', 'actors', 'image']

class MoviePosterDelete(DeleteView):
  model = MoviePoster
  success_url='/movieposter/'

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def movieposter_index(request):
  movieposters = MoviePoster.objects.all()
  return render(request, 'movieposter/index.html', {'movieposters': movieposters})

def movieposter_detail(request, movieposter_id):
  movie = MoviePoster.objects.get(id=movieposter_id)
  rating_form = RatingForm()
  return render(request,'movieposter/detail.html', {'movie':movie, 'rating_form':rating_form})

def add_rating(request, movieposter_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit = False)
    new_rating.movieposter_id = movieposter_id
    new_rating.save()
  return redirect('detail', movieposter_id=movieposter_id) 