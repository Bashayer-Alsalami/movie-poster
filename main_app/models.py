from django.db import models

# Create your models here.
class MoviePoster(models.Model):
  name = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=250)
  duration = models.DurationField()
  actors = models.CharField(max_length=100)
  image = models.ImageField(upload_to ="main_app/static/uploads", default="")