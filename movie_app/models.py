from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=50)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

