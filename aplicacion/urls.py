from django.urls import path
from .views import ListSong , SearchView

urlpatterns = [
    path('', ListSong.as_view(), name='home'),
    path('search', SearchView.as_view(),name='search'),
]
