from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movieposter/', views.movieposter_index, name='index'),
  path('movieposter/<int:movieposter_id>', views.movieposter_detail, name='detail'),
  path('movieposter/create', views.MoviePosterCreate.as_view(), name='movieposter_create'),
  path('movieposter/<int:pk>/update/', views.MoviePosterUpdate.as_view(), name='movieposter_update'),
  path('movieposter/<int:pk>/delete', views.MoviePosterDelete.as_view(), name='movieposter_delete'),
  path('movieposter/<int:movieposter_id>/add_rating', views.add_rating, name='add_rating'),

  # Actor urls
  path('actors/', views.ActorList.as_view(), name='actors_index'),
  path('actors/<int:pk>/', views.ActorDetail.as_view(), name='actors_detail'),
  path('actors/create/', views.ActorCreate.as_view(), name='actors_create'),
  path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actors_update'),
  path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actors_delete'),

    # assosiate a toy with a cat
  path('movieposter/<int:movieposter_id>/assoc_actor/<int:actor_id>/', views.assoc_actor, name='assoc_actor'),

    # unassosiate a toy with a cat
  path('movieposter/<int:movieposter_id>/unassoc_actor/<int:actor_id>/', views.unassoc_actor, name='unassoc_actor'),
  
    path('accounts/signup/', views.signup, name='signup')

]