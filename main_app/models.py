from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

RANKING=(
  ('A', 'Excellent'),
  ('B', 'Good'),
  ('C', 'Average'),
  ('D', 'Poor')
)

class Actor(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('actors_detail', kwargs={'pk': self.id})

class MoviePoster(models.Model):
  name = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  duration = models.DurationField()
  image = models.ImageField(upload_to ="main_app/static/uploads", default="")
  actors = models.ManyToManyField(Actor)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'movieposter_id': self.id} )

  def __str__(self):
    return f"{self.name}"

  # def rate_for_today(self):
  #   return self.rating_set.filter(date=date.today()).count() >= ()

  def rate_movie(self):
    return self.rating_set.filter(rank='A').count()

class Rating(models.Model):
  date = models.DateField('Rating Date')
  rank = models.CharField(max_length=1, choices=RANKING, default=RANKING[0][0])
  movieposter = models.ForeignKey(MoviePoster, on_delete=models.CASCADE)


# 
  def __str__(self):
    return f"{self.movieposter.name} {self.get_rank_display()} on {self.date}"


  class Meta:
    # ordering = ['date']  #Date ascending
    ordering = ['-date']  #Date descending

