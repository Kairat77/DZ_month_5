from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers


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