from cmath import exp
from curses.ascii import isspace
import spotipy
from spotipy import oauth2
from Vibeland_api.constants.constants import LIBRARY_SCOPES
from Vibeland_api.secrets.secrets import *
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response
from Vibeland_backend.Vibeland_api.spotify.spotify_utils import is_spotify_authenticated
from spotify_utils import update_or_create_user_tokens
from django.shortcuts import redirect

class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = LIBRARY_SCOPES

        #Request authorization from Spotify
        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)

def spotifyCallback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://account.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    #Extract the information we need from the response
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(
        session_id=request.session.session_key, access_token=token_type, 
        token_type=token_type, expires_in=expires_in)
    
    return redirect('')

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_spotify_authenticated = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_spotify_authenticated}, status=status.HTTP_200_OK)