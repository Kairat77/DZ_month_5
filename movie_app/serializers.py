from rest_framework import serializers
from movie_app.models import Director, Movie, Review, Rating
from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError







class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "stars".split()


class ReviewSerializers(serializers.ModelSerializer):
    rating = RatingSerializers()
    class Meta:
        model = Review
        fields = " id text movie rating ".split()


class MovieSerializers(serializers.ModelSerializer):
    review_set = ReviewSerializers(many=True)
    class Meta:
        model = Movie
        fields = "id title description duration director review_set".split()


class DirectorSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    def get_movies_count(self, director):
        return director.movies.count()
    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=4, max_length=20, validators=[
            RegexValidator(r'^[a-zA-Z\s]*$', 'Введите только текст (буквы и пробелы).')
        ])


class MovieValidateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=4,max_length=100)
    description = serializers.CharField(required=False, default='No Text')
    duration = serializers.CharField(max_length=50)
    director_id = serializers.IntegerField(min_value=1)
    review_set = serializers.ListField(child=serializers.IntegerField())  # Список с id отзывов

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return director_id
    
class ReviewValidateSerializers(serializers.Serializer):
    text = serializers.CharField( required=False, default='No Text')
    movie_id = serializers.IntegerField(min_value=1)
    rating_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist!')
        return movie_id
    
    def validate_rating_id(self, rating_id):
        try:
            Rating.objects.get(id=rating_id)
        except Rating.DoesNotExist:
            raise ValidationError('Rating does not exist!')
        return rating_id
    
