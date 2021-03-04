from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from API.models import Movie


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'

