from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from Vibeland_api.spotify_control_center import clientCredentialsFlow, authorizationCodeFlow
import Vibeland_api.spotify_control_center
from Vibeland_api.recommender.recommend_engine import *
from rest_framework.decorators import api_view
import json

from Vibeland_api.recommender.recommend_engine import recommendationEngine
from Vibeland_api.recommender import *

def index():
    pass

def initializeDeveloperAccess():
    clientCredentialsFlow()

@api_view(['GET', 'POST'])
def accessRecommendationSystem(request):
    spotify_api_accessor = authorizationCodeFlow(request.data["credentials"])
    if request.method == 'POST':
        if request.data["type"] == "explore":
            recommendationEngine(spotify_api_accessor)
            return HttpResponse("KKKKKKK")
