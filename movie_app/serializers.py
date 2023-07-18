from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Director
        fields = 'name'.split()

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = 'title description duration director'.split()

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields = 'text movie'.split()


