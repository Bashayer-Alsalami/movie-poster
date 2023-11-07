from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MoviePoster, Actor
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


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

@login_required
def movieposter_index(request):
  movieposters = MoviePoster.objects.filter(user=request.user)
  return render(request, 'movieposter/index.html', {'movieposters': movieposters})

@login_required
def movieposter_detail(request, movieposter_id):
  movie = MoviePoster.objects.get(id=movieposter_id)
  rating_form = RatingForm()
  actors_movie_dosent_have = Actor.objects.exclude(id__in = movie.actors.all().values_list('id'))
  # print(actors_movie_dosent_have)
  return render(request,'movieposter/detail.html', {'movie':movie, 'rating_form':rating_form, 'actors': actors_movie_dosent_have})

@login_required
def add_rating(request, movieposter_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit = False)
    new_rating.movieposter_id = movieposter_id
    new_rating.save()
  return redirect('detail', movieposter_id=movieposter_id) 

# CRUD operation for Actors

class ActorList(LoginRequiredMixin, ListView):
  model = Actor

class ActorDetail(LoginRequiredMixin, DetailView):
  model = Actor

class ActorCreate(LoginRequiredMixin, CreateView):
  model = Actor
  fields = ['name', 'age']

class ActorUpdate(LoginRequiredMixin, UpdateView):
  model = Actor
  fields = ['name', 'age']

class ActorDelete(LoginRequiredMixin, DeleteView):
  model = Actor
  success_url = '/actors/'

@login_required
def assoc_actor(request, movieposter_id, actor_id):
  # Add this toy_id with the cat selected (cat_id)
  MoviePoster.objects.get(id=movieposter_id).actors.add(actor_id)
  return redirect('detail', movieposter_id=movieposter_id)

@login_required
def unassoc_actor(request, movieposter_id, actor_id):
  # Add this toy_id with the cat selected (cat_id)
  MoviePoster.objects.get(id=movieposter_id).actors.remove(actor_id)
  return redirect('detail', movieposter_id=movieposter_id)

def signup(request):
  error_message =''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # passing the user to login so it can work when user enter username and password
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup - Please Try Again Later', form.error_messages


  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)