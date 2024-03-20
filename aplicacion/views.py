from django.db.models import Q , Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView , View , DetailView , UpdateView , DeleteView , CreateView ,TemplateView
from .models import Song , Artist , Review , User 
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
# Create your views here.

class ListSong(ListView):
    model = Song
    template_name = 'aplicacion/home.html'
    context_object_name = 'Song'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['most_reviewed_songs'] = Song.objects.annotate(num_reviews=Count('review')).order_by('-num_reviews')[:5]

        # Verificar si el usuario está autenticado antes de acceder a sus amigos
        if self.request.user.is_authenticated:
            # Si el usuario está autenticado, obtener los amigos y sus comentarios
            friends = self.request.user.friends.all()
            friends_comments = Review.objects.filter(author__in=friends)
            friends_songs = [comment.song for comment in friends_comments]
            context['friend_song'] = friends_songs
        else:
            # Si el usuario no está autenticado, establecer friend_song como una lista vacía
            context['friend_song'] = []

        return context

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
    success_url=reverse_lazy('home')

class DeleteSong(DeleteView):
    model= Song
    template_name ='aplicacion/delete.html'
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

class DetailArtist(DetailView):
    model = Artist
    template_name= 'aplicacion/artistDetail.html'

class CreateArtist(CreateView):
    model = Artist
    template_name= 'aplicacion/createArtist.html'
    fields = ['name','born','biography','picture','group']
    success_url = reverse_lazy('artists')

class EditArtist(UpdateView):
    model = Artist
    template_name= 'aplicacion/editArtist.html'
    fields = ['name','born','biography','picture','group']
    success_url = reverse_lazy('artists')

class DeleteArtist(DeleteView):
    model = Artist
    template_name = 'aplicacion/deleteArtist.html'
    success_url = reverse_lazy('artists')


class RegisterView(View):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado con éxito")
            return redirect("home")
        else:
            messages.error(request, "Error en el registro, la información proporcionada no es válida")

        return render(request, self.template_name, {'form': form})
    
class CreateReview(CreateView):
    model = Review
    template_name = 'aplicacion/create_review.html'
    fields = ['opinion']
    success_url = reverse_lazy("home")

    def get(self, request, pk):
        author = self.request.user
        song = Song.objects.get(pk=pk)
        review = Review.objects.filter(song=song, author=author).first()

        if review:
            form = ReviewForm(instance=review)
        else:
            form = ReviewForm()

        return render(request, self.template_name, {'review': review, 'song': song, 'form': form, 'author': author})

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        song = Song.objects.get(pk=pk)
        author = self.request.user

        existe_Review = Review.objects.filter(song=song, author=author).first()

        if existe_Review:
            form = ReviewForm(request.POST, instance=existe_Review)
        else:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.song = song
            review.author = author
            review.save()

            return redirect('home')

        return render(request, 'aplicacion/create_review.html', {'song': song, 'form': form, 'author': author})
    
class ViewReview(View):
    model = Review
    template_name = 'aplicacion/review.html'
    context_object_name = 'reviews'

    def get(self, request, pk):
        song = Song.objects.get(pk=pk)
        reviews = Review.objects.filter(song=song)
        return render(request, self.template_name, {'reviews': reviews})
    
class ProfileView(TemplateView):
    model = User
    template_name = 'aplicacion/profile.html'
    context_objcet_name = 'Users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user 
        context['friends'] = self.request.user.friends.all()
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)
    
class EditProfile(UpdateView):
    model = User
    template_name = 'aplicacion/editProfile.html'
    fields = ["username","first_name","last_name","email","photo"]
    success_url = reverse_lazy("profile")

class AddFirend(UpdateView):
    model = User
    template_name = 'aplicacion/addFriend.html'
    fields = ["friends"]
    success_url = reverse_lazy("profile")