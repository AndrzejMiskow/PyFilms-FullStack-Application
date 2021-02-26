import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(default=0 , primary_key = True)
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    cast_members = models.CharField(max_length = 256)
    description = models.CharField(max_length=256)
    movie_poster = models.ImageField(upload_to='Movie_images', blank = True)
    movie_duration = models.IntegerField(default = 1)
    tickets_sold = models.IntegerField(default= 0)


    def __str__(self):
        return self.movie_text
