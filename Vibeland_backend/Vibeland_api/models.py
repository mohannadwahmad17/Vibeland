from django.db import models

#This is the model that represents a Song item in the database
class Song(models.Model):
    name = models.CharField(max_length=100)
    danceability = models.FloatField(default=0.0)
    energy = models.FloatField(default=0.0)
    key = models.FloatField(default=0.0)
    loudness = models.FloatField(default=0.0)
    mode = models.FloatField(default=0.0)
    speechness = models.FloatField(default=0.0)
    acousticness = models.FloatField(default=0.0)
    instrumentalness = models.FloatField(default=0.0)
    liveness = models.FloatField(default=0.0)
    valence = models.FloatField(default=0.0)
    tempo = models.FloatField(default=0.0)
    type = models.CharField(max_length=50, default="")
    trackid = models.CharField(max_length=100, default="")
    uri = models.CharField(max_length=100, default="")
    ref_track = models.URLField(default="")
    url_features = models.URLField(default="")
    duration = models.IntegerField(default=0)
    time_signature = models.IntegerField(default=0)
    genre = models.CharField(max_length=100, default="")