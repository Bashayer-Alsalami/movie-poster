from django.forms import ModelForm
from .models import Rating

class RatingForm(ModelForm):
  # it needed for custome model form (to not provide fields like CBV)
  class Meta:
    model = Rating
    fields = ['date', 'rank']