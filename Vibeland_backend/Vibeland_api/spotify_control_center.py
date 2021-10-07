import spotipy
from spotipy.client import Spotify
from constants import constants
from spotipy.oauth2 import SpotifyClientCredentials

spotify_api_accessor = None

def getDevAccessToSpotifyWebAPI():
    client_credentials_manager = SpotifyClientCredentials(constants.CLIENT_ID, constants.CLIENT_SECRET)
    spotify_api_accessor = Spotify(client_credentials_manager)

def handleCredentials(credentials):
    
    pass