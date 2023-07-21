from rest_framework import serializers
from movie_app.models import Director, Movie, Review, Rating


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "name".split()





class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "stars".split()


class ReviewSerializers(serializers.ModelSerializer):
    rating = RatingSerializers()
    class Meta:
        model = Review
        fields = "text movie rating ".split()


class MovieSerializers(serializers.ModelSerializer):
    review_set = ReviewSerializers(many=True)
    class Meta:
        model = Movie
        fields = "title description duration director review_set".split()


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, director):
        return Movie.objects.filter(director=director).count()

    class Meta:
        model = Director
        fields = ('name', 'movies_count')