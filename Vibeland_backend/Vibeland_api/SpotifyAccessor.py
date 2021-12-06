#This class defines the spotify accessor object and access token needed to interface with API
class SpotifyAccessor:
    def __init__(self, spotifyAccessor, token):
        self.spotifyAccessor = spotifyAccessor
        self.token = token