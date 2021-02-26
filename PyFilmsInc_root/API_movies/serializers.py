# serializers.py

from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ('movie_id', 'title', 'director', 'cast_members', 'description',
              'movie_poster', 'movie_duration', 'tickets_sold')
