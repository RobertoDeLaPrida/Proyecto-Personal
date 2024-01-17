from django.urls import path
from .views import (ListSong,
                    SearchView,
                    DetailSong,
                    EditSong,
                    DeleteSong,
                    CreateSong,
                    ArtistView,
                    ArtistDetail)

urlpatterns = [
    path('', ListSong.as_view(), name='home'),
    path('search/', SearchView.as_view(),name='search'),
    path('detail/<int:pk>', DetailSong.as_view(), name='detail'),
    path('edit/<int:pk>', EditSong.as_view(),name='edit'),
    path('delete/<int:pk>', DeleteSong.as_view(),name='delete'),
    path('create/', CreateSong.as_view(),name='create'),
    path('artists/',ArtistView.as_view(),name='artists'),
    path('artist/detail/<int:pk>',ArtistDetail.as_view(),name='artistDetail')

]
