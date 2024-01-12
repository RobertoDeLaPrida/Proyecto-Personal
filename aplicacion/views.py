from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView , View
from .models import Song 

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
    
