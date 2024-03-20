from django import views
from django.urls import path
from .views import (ListSong,
                    SearchView,
                    DetailSong,
                    EditSong,
                    DeleteSong,
                    CreateSong,
                    ArtistView,
                    DetailArtist,
                    CreateArtist,
                    EditArtist,
                    DeleteArtist,
                    RegisterView,
                    CreateReview,
                    ViewReview,
                    ProfileView,
                    EditProfile,
                    AddFirend)
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 

urlpatterns = [
    path('', ListSong.as_view(), name='home'),
    path('search/', SearchView.as_view(),name='search'),
    path('detail/<int:pk>', DetailSong.as_view(), name='detail'),
    path('edit/<int:pk>', EditSong.as_view(),name='edit'),
    path('delete/<int:pk>', DeleteSong.as_view(),name='delete'),
    path('create/', CreateSong.as_view(),name='create'),
    path('artists/',ArtistView.as_view(),name='artists'),
    path('artist/detail/<int:pk>',DetailArtist.as_view(),name='artistDetail'),
    path('artist/create/',CreateArtist.as_view(),name='createArtist'),
    path('artist/edit/<int:pk>',EditArtist.as_view(),name='editArtist'),
    path('artist/delete/<int:pk>',DeleteArtist.as_view(),name='deleteArtist'),
    path('register/', RegisterView.as_view(), name='register'),
    path('create_review/<int:pk>/', login_required(CreateReview.as_view()),name='create_review'),
    path('review/<int:pk>/',ViewReview.as_view(), name='review'),
    path('profile',login_required(ProfileView.as_view()),name='profile'),
    path('profile/edit/<int:pk>',EditProfile.as_view(), name='editProfile'),
    path('profile/edit/<int:pk>/friends', AddFirend.as_view(), name='addFriend')
]
