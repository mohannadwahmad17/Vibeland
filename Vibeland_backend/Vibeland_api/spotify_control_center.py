import spotipy
import spotipy.util as util
from spotipy.client import Spotify
from Vibeland_api.firebase import *
from Vibeland_api.secrets.secrets import *
from Vibeland_api.constants.constants import *
from spotipy.oauth2 import SpotifyClientCredentials
from Vibeland_api.SpotifyAccessor import SpotifyAccessor

spotify_api_accessor = None

#This form of authorization is for the general spotify web api and not for user data
def clientCredentialsFlow():
    client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    spotify_api_accessor = Spotify(client_credentials_manager)

#This obtains the user authentication token to access user Spotify information
def authorizationCodeFlow(credentials):
    #Define the scopes that the accessor would have when accessing user data
    scopes = USER_SCOPES + ", " + SPOTIFY_CONNECT_SCOPES + ", " +  LIBRARY_SCOPES + ", " + LISTENING_HISTORY_SCOPES

    #Store the access token once approved by the user
    token = util.prompt_for_user_token(username=credentials["username"], scope=scopes, 
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, show_dialog=True)

    #Make sure the token is valid then store it and return it for future use
    try:
        if token:
            print(token)
            accessor = spotipy.Spotify(auth=token)
            spotify_api_accessor = SpotifyAccessor(accessor, token)

            return spotify_api_accessor
        else:
            return "Error with access token!"
    except:
        print("Error authentication access token!")
        return None