import spotipy
import spotipy.util as util
from spotipy.client import Spotify
from Vibeland_api.constants.constants import *
from spotipy.oauth2 import SpotifyClientCredentials

spotify_api_accessor = None

def clientCredentialsFlow():
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    spotify_api_accessor = Spotify(client_credentials_manager)

def authorizationCodeFlow(credentials):
    clientCredentialsFlow()

    scopes = USER_SCOPES + " " + SPOTIFY_CONNECT_SCOPES + " " +  LIBRARY_SCOPES + " " + LISTENING_HISTORY_SCOPES
    token = util.prompt_for_user_token(username=credentials["username"], scope=scopes, 
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

    if token:
        spotify = spotipy.Spotify(auth=token)
        results = spotify.current_user_saved_tracks()