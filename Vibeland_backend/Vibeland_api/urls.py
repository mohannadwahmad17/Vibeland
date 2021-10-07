from django.urls import path, include
from . import views
from django.urls import path

url_patterns = [
    path('spotifyDevAccess/', views.initializeDeveloperAccess, name="developerAccessHandler"),
    path('spotifyUserLogin/', views.loginToSpotify, name="spotifyLoginHandler")
]