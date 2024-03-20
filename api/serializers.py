from aplicacion.models import Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title','artist','lyrics','release_date','cover','SpotifyLink','YoutubeLink','SoundcloudLink')