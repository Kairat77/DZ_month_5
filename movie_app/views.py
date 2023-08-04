from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import (
    DirectorSerializers,
    MovieSerializers,
    ReviewSerializers,
)
from rest_framework import status


@api_view(["GET", "POST"])
def director_view(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializers(directors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        name = request.data.get("name")
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializers(director).data)


# @api_view(["GET", "POST"])
# def director_view(request):
#     if request.method == "GET":
#         director = Director.objects.all()
#         data = DirectorSerializers(instance=director, many=True).data
#         return Response(data=data)


@api_view(["GET", "PUT", "DELETE"])
def director_id_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={"message:" "ошибка фронтеншика"}, status=404)
    if request.method == "GET":
        data = DirectorSerializers(instance=director, many=False).data
        return Response(data=data)
    elif request.method == "PUT":
        director.name = request.data.get("name")
        director.movies_count = request.data.get("movies_count")
        return Response(data=DirectorSerializers(director).data)
    else:
        director.delete()
        return Response(status=204)


@api_view(["GET", "POST"])
def movies_view(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        data = MovieSerializers(instance=movie, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        title = request.data.get("title")
        description = request.data.get("description")
        duration = request.data.get("duration")
        director_id = request.data.get("director")
        movies = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id,
        )
        return Response(data=MovieSerializers(movies).data)


@api_view(["GET", "PUT", "DELETE"])
def movies_id_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={"message:" "ошибка фронтеншика"}, status=404)
    if request.method == 'GET':
        data = MovieSerializers(instance=movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        return Response(data=MovieSerializers(movie).data)
    else:
        movie.delete()
        return Response(status=204)
        



@api_view(["GET","POST"])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializers(instance=review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get("text")
        movie_id = request.data.get("movie")
        rating_id = request.data.get("rating")
        review = Review.objects.create(
            text=text, movie_id=movie_id, rating_id=rating_id
        )
        return Response(data=ReviewSerializers(review).data)


@api_view(["GET", "PUT", "DELETE"])
def review_id_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"message:" "ошибка фронтеншика"}, status=404)
    if request.method == 'GET':
        data = ReviewSerializers(instance=review, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie')
        review.rating_id = request.data.get('rating')
        return Response(data=ReviewSerializers(review).data)
    else:
        review.delete()
        return Response(status=204)


@api_view(["GET"])
def movie_reviews_view(request):
    # Fetch all movies with their reviews
    movies = Movie.objects.prefetch_related("review_set").all()

    # Calculate the average rating of all reviews
    reviews = Review.objects.all()
    total_ratings = sum(review.rating.stars for review in reviews)
    average_rating = total_ratings / reviews.count() if reviews.count() > 0 else 0

    # Serialize the data
    serializer = MovieSerializers(movies, many=True)

    data = {
        "movies": serializer.data,
        "average_rating": average_rating,
    }

    return Response(data, status=status.HTTP_200_OK)
