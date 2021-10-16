from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    danceability = models.FloatField(default=0.0)
    energy = models.FloatField(default=0.0)
    key = models.IntegerField(default=0)
    loudness = models.FloatField(default=0.0)
    mode = models.IntegerField(default=0)
    speechness = models.FloatField(default=0.0)
    acousticness = models.FloatField(default=0.0)
    instrumentalness = models.FloatField(default=0.0)
    liveness = models.FloatField(default=0.0)
    valence = models.FloatField(default=0.0)
    tempo = models.FloatField(default=0.0)
    id = models.CharField(default="")
    uri = models.CharField(default="")
    ref_track = models.URLField(default="")
    url_features = models.URLField(default="")
    duration = models.IntegerField(default=0)
    time_signature = models.IntegerField(default=0)
    genre = models.CharField(default="")