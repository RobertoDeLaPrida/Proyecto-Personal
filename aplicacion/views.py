from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , View , DetailView , UpdateView , DeleteView , CreateView
from .models import Song , Artist

# Create your views here.

class ListSong(ListView):
    model = Song
    template_name = 'aplicacion/home.html'
    context_object_name = 'Song'

class SearchView(View):
    model = Song
    template_name = 'aplicacion/search.html'
    context_object_name = 'Song'
    def get(self, request):
        query = request.GET.get('Buscar')

        if query:
            results = Song.objects.filter(Q(title__icontains=query) | Q(artist__name__icontains=query))
            return render(request, self.template_name, {'results': results, 'query': query})
        return render(request, self.template_name, {'query': query})
    

class DetailSong(DetailView):
    model= Song
    template_name = 'aplicacion/detail.html'

class EditSong(UpdateView):
    model= Song
    fields=['title','artist','lyrics','release_date','cover','SpotifyLink','YoutubeLink','SoundcloudLink']
    template_name='aplicacion/edit.html'
    success_url=reverse_lazy('index')

class DeleteSong(DeleteView):
    model= Song
    template_name ='aplicacin/delete.html'
    success_url = reverse_lazy('home')

class CreateSong(CreateView):
    model= Song
    fields=['title','artist','lyrics','release_date','cover','SpotifyLink','YoutubeLink','SoundcloudLink']
    template_name = 'aplicacion/create.html'
    success_url = reverse_lazy('home')

class ArtistView(ListView):
    model = Artist
    template_name='aplicacion/artists.html'
    context_object_name = 'Artist'

class ArtistDetail(DetailView):
    model = Artist
    template_name= 'aplicacion/artistDetail.html'