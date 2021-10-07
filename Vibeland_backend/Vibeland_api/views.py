from django.shortcuts import render
from django.http import HttpResponse
from Vibeland_backend.Vibeland_api.spotify_control_center import getDevAccessToSpotifyWebAPI
import spotify_control_center

def initializeDeveloperAccess():
    getDevAccessToSpotifyWebAPI()

def loginToSpotify():
    return HttpResponse("LOL");