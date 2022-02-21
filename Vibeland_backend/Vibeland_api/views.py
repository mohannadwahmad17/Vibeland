from Vibeland_api.spotify_control_center import authorizationCodeFlow
from Vibeland_api.spotify.authorization import AuthURL
from Vibeland_api.recommender.recommend_engine import recommendationEngine
from Vibeland_api.recommender.recommend_engine import *
from rest_framework.decorators import api_view
from Vibeland_api.recommender import *
from django.http import HttpResponse
from django.shortcuts import render
import json

def index():
    pass

#Perform client credentials authorization flow
def initializeDeveloperAccess():
    # clientCredentialsFlow()
    return HttpResponse("POP")

# def authorizeAppAccessToUserSpotifyData(request):
#     authorizationCodeFlow()

#This method directs POST and GET requests to their appropriate endpoints to retrieve song recommendations for the user
@api_view(['GET', 'POST'])
def accessRecommendationSystem(request):
    #Prompt the user to authorize Vibeland to retrieve their song data
    spotify_api_accessor = authorizationCodeFlow(request.data["credentials"])

    #This is where POST requests are sent from this method
    if request.method == 'POST':
        #Determine if the POST request is to explore music
        if request.data["type"] == "explore":
            #Begin the process of analyzing the user's song data and retrieving recommendations
            songs = recommendationEngine(spotify_api_accessor)

            #This json object contains the list of the user's songs as well as the accessor token
            songs_json = {
                "songs" : songs,
                "token" : spotify_api_accessor.token
            }
            return HttpResponse(json.dumps(songs_json))
    
    if request.method == 'GET':
        return HttpResponse("LOL")