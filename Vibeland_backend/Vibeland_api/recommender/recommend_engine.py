
def recommendationEngine(spotifyApiAccessor):
    #Get the current user's song library
    user_song_library = getUserSongLibrary(spotifyApiAccessor)

    print(user_song_library)

def getUserSongLibrary(spotifyApiAccessor):
    user_library = spotifyApiAccessor.get_current_user_saved_tracks()

    return user_library
