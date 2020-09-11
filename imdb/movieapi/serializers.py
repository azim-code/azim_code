from rest_framework import serializers

from .models import Movies , Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'