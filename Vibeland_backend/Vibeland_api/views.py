from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from Vibeland_api.spotify_control_center import clientCredentialsFlow, authorizationCodeFlow
import Vibeland_api.spotify_control_center
from rest_framework.decorators import api_view
import json

def index():
    pass

def initializeDeveloperAccess():
    clientCredentialsFlow()

@api_view(['GET', 'POST'])
def loginToSpotify(request):
    if request.method == 'POST':
        print(request.data)
        authorizationCodeFlow(request.data["credentials"])
        return HttpResponse("KKKKKKK")
