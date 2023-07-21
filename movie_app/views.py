from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers
from rest_framework import status

@api_view(['GET'])
def director_view(request):
    name = Director.objects.all()
    data = DirectorSerializers(instance=name, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_id_view(request, id):
    try:
      name = Director.objects.get(id=id)
    except Director.DoesNotExist:
      return Response(data={'message:''ошибка фронтеншика'}, status=404)
    data=DirectorSerializers(instance=name, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
   movie = Movie.objects.all()
   data = MovieSerializers(instance=movie, many=True).data
   return Response(data=data)


@api_view(['GET'])
def movies_id_view(request, id):
    try:
      movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
       return Response(data={'message:''ошибка фронтеншика'}, status=404)
    data=MovieSerializers(instance=movie, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_view(request):
   review = Review.objects.all()
   data = ReviewSerializers(instance=review, many=True).data
   return Response(data=data)


@api_view(['GET'])
def review_id_view(request, id):
    try:
      review = Review.objects.get(id=id)
    except Review.DoesNotExist:
      return Response(data={'message:''ошибка фронтеншика'}, status=404)
    data=ReviewSerializers(instance=review, many=False).data
    return Response(data=data)


@api_view(['GET'])
def movie_reviews_view(request):
    # Fetch all movies with their reviews
    movies = Movie.objects.prefetch_related('review_set').all()

    # Calculate the average rating of all reviews
    reviews = Review.objects.all()
    total_ratings = sum(review.rating.stars for review in reviews)
    average_rating = total_ratings / reviews.count() if reviews.count() > 0 else 0

    # Serialize the data
    serializer = MovieSerializers(movies, many=True)

    data = {
        'movies': serializer.data,
        'average_rating': average_rating,
    }

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializers(directors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
