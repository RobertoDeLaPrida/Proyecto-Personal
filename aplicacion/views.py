from django.shortcuts import render
from django.views.generic import ListView
from .models import Song

# Create your views here.

class ListSong(ListView):
    model = Song
    template_name = 'aplicacion/home.html'
