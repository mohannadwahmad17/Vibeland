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
    scopes = USER_SCOPES + " " + SPOTIFY_CONNECT_SCOPES + " " +  LIBRARY_SCOPES + " " + LISTENING_HISTORY_SCOPES
    token = util.prompt_for_user_token(username=credentials["username"], scope=scopes)
    pass