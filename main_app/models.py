from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

RANKING=(
  ('A', 'Excellent'),
  ('B', 'Good'),
  ('C', 'Average'),
  ('D', 'Poor')
)


class MoviePoster(models.Model):
  name = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  duration = models.DurationField()
  actors = models.CharField(max_length=100)
  image = models.ImageField(upload_to ="main_app/static/uploads", default="")

  def get_absolute_url(self):
    return reverse('detail', kwargs={'movieposter_id': self.id} )

    def __str__(self):
      return f"{self.name}"
  


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

