from django.urls import path, include
from Vibeland_api import views

url_patterns = [
    path('', views.index, name='index'),
    path('spotifyDevAccess/', views.initializeDeveloperAccess, name="developerAccessHandler"),
    path('spotifyUserLogin/', views.loginToSpotify, name="spotifyLoginHandler")
]