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
  path('movieposter/<int:movieposter_id>/add_rating', views.add_rating, name='add_rating')
]