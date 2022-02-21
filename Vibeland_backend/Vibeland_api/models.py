from django.db import models
from django.db.models.fields import DateTimeField
from stream_django.activity import Activity

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
    centroid = models.IntegerField(default=0)

class RecommendationCard(models.Model, Activity):
    created_at = models.DateTimeField(auto_now_add=True)
    artist_name = models.CharField(default="", max_length=100)
    song_name = models.CharField(default="", max_length=100)

    @property
    def activity_actor_attr(self):
        return self.song_name

class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)