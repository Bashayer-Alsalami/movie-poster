from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movieposter/', views.movieposter_index, name='index'),
  path('/movieposter/<int:movie_id>', views.movieposter_detail, name='detail')
]