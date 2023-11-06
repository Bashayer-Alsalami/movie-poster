from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MoviePoster, Actor
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
  fields = ['name', 'year', 'duration', 'description', 'image']

class MoviePosterUpdate(UpdateView):
  model = MoviePoster
  fields = ['name', 'year', 'duration', 'description', 'image']

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
  actors_movie_dosent_have = Actor.objects.exclude(id__in = movie.actors.all().values_list('id'))
  return render(request,'movieposter/detail.html', {'movie':movie, 'rating_form':rating_form, 'actors_movie_dosent_have': actors_movie_dosent_have})

def add_rating(request, movieposter_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit = False)
    new_rating.movieposter_id = movieposter_id
    new_rating.save()
  return redirect('detail', movieposter_id=movieposter_id) 

# CRUD operation for Actors

class ActorList(ListView):
  model = Actor

class ActorDetail(DetailView):
  model = Actor

class ActorCreate(CreateView):
  model = Actor
  fields = ['name', 'age']

class ActorUpdate(UpdateView):
  model = Actor
  fields = ['name', 'age']

class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors/'

def assoc_actor(request, movieposter_id, actor_id):
  # Add this toy_id with the cat selected (cat_id)
  MoviePoster.objects.get(id=movieposter_id).actors.add(actor_id)
  return redirect('detail', movieposter_id=movieposter_id)


def unassoc_actor(request, movieposter_id, actor_id):
  # Add this toy_id with the cat selected (cat_id)
  MoviePoster.objects.get(id=movieposter_id).actors.remove(actor_id)
  return redirect('detail', movieposter_id=movieposter_id)