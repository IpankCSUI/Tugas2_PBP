from django.db import models

# Create your models here.
class FilmWatchlist(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()