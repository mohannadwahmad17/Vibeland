from Vibeland_api.recommender.algorithms import *

def recommendationEngine(spotifyApiAccessor):
    #Get the current user's song library
    user_song_library, song_ids = getUserSongLibrary(spotifyApiAccessor)

    #Retrieve the audio features of each of the songs in the user's library
    user_song_features = getUserSongFeatures(spotifyApiAccessor, song_ids)

    #Run the audio features for each song through the kmenas clustering algorithm to analyze the data
    # recommendations = kmeans_clustering(user_song_features, 5, 5)

    return user_song_library

def getUserSongLibrary(spotifyApiAccessor):
    user_library = spotifyApiAccessor.current_user_saved_tracks(limit=50)
   
    song_ids = []
    song_tuples = []

    for item in user_library['items']:
        track = item['track']

        song_tuple = {
            "title": track['name'], 
            "artists": track['artists'][0]['name']
        }
        song_tuples.append(song_tuple)
        song_ids.append(track['id'])

    return song_tuples, song_ids

def getUserSongFeatures(spotifyApiAccessor, song_ids):
    song_features = spotifyApiAccessor.audio_features(song_ids)
    song_features_final_list = []

    song_features_final_list.append(list(song_features[0].keys()))

    for features in song_features:
        song_features_final_list.append(list(features.values()))
    
    return song_features_final_list