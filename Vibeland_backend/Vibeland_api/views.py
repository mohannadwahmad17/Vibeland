from django.shortcuts import render
from django.http import HttpResponse
from Vibeland_backend.Vibeland_api.spotify_control_center import clientCredentialsFlow, authorizationCodeFlow
import spotify_control_center

def initializeDeveloperAccess():
    clientCredentialsFlow()

def loginToSpotify(data):
    authorizationCodeFlow(data["credentials"])
    return HttpResponse("LOL");