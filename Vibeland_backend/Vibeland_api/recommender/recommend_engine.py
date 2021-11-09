
def recommendationEngine(spotifyApiAccessor):
    #Get the current user's song library
    user_song_library = getUserSongLibrary(spotifyApiAccessor)

    return user_song_library

def getUserSongLibrary(spotifyApiAccessor):
    user_library = spotifyApiAccessor.current_user_saved_tracks(limit=50)
    print(user_library)
    song_artist_tuples = []
    for item in user_library['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
        song_artist_tuple = {
            "title": track['name'], 
            "artists": track['artists'][0]['name']
        }
        song_artist_tuples.append(song_artist_tuple)

    return song_artist_tuples
