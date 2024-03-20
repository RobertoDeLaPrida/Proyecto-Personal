from django.shortcuts import render
from .serializers import SongSerializer
from rest_framework import viewsets, permissions
from aplicacion.models import Song

# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [ permissions.IsAdminUser ]
