from django.shortcuts import HttpResponse
from rest_framework import viewsets

from .serializers import *
from .models import *

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('movie_id')
    serializer_class = MovieSerializer

