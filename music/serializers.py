from rest_framework import fields, serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('ism','rasm')

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('id','nom','cover','source')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('id','nom','muqova')