import spotipy
import spotipy.util as util
from spotipy.client import Spotify
from Vibeland_api.firebase import *
from Vibeland_api.secrets.secrets import *
from Vibeland_api.constants.constants import *
from spotipy.oauth2 import SpotifyClientCredentials

spotify_api_accessor = None

def clientCredentialsFlow():
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    spotify_api_accessor = Spotify(client_credentials_manager)

#This obtains the user authentication token to access user Spotify information
def authorizationCodeFlow(credentials):
    scopes = USER_SCOPES + ", " + SPOTIFY_CONNECT_SCOPES + ", " +  LIBRARY_SCOPES + ", " + LISTENING_HISTORY_SCOPES
    token = util.prompt_for_user_token(username=credentials["username"], scope=scopes, 
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

    try:
        if token:
            spotify_api_accessor = spotipy.Spotify(auth=token)
            return spotify_api_accessor
        else:
            return "Error with access token!"
    except:
        print("Error authentication access token!")
        return None