from django.urls import path
from .views import ListSong

urlpatterns = [
    path('', ListSong.as_view(), name='home'),
]
