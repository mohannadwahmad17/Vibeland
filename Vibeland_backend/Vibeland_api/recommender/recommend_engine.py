from Vibeland_api.constants.constants import CENTROIDS
from Vibeland_api.recommender.algorithms import *
from Vibeland_api.models import Song
import csv

#This is the central function that calls the methods to perform the song library analysis and song recommendation process
def recommendationEngine(spotifyApiAccessor):
    #Get the current user's song library
    user_song_library, song_ids = getUserSongLibrary(spotifyApiAccessor)

    #Retrieve the audio features of each of the songs in the user's library
    user_song_features = getUserSongFeatures(spotifyApiAccessor, song_ids)

    #Run the audio features for each song through the kmenas clustering algorithm to analyze the data
    clusters = closest_centroid(CENTROIDS, user_song_features)

    #Using the clusters obtained from the algorithm, query the song DB for appropriate song recommendations
    recommendations = get_recommendations(clusters)

    return user_song_library

#This function uses the spotify API to get the current user's song library along with extra details to be shown on the frontend
def getUserSongLibrary(spotifyApiAccessor):
    #Get the current user's saved song library
    user_library = spotifyApiAccessor.spotifyAccessor.current_user_saved_tracks(limit=50)
   
    song_ids = []
    song_tuples = []

    #Extract the relevant information from the retrieved list of song items
    for item in user_library['items']:
        track = item['track']

        song_tuple = {
            "title": track['name'],
            "songuri": track['uri'],
            "songprev": track['preview_url'],
            "token": spotifyApiAccessor.token,
            "artists": track['artists'][0]['name'],
            "songurl": track['external_urls']['spotify'],
            "coverart": track['album']['images'][0]['url'],
        }
        
        song_tuples.append(song_tuple)
        song_ids.append(track['id'])

    return song_tuples, song_ids

#Remove the unneeded audio features from the data
def clean_data(data):
    del(data[11:18])
    del(data[6])
    del(data[3])
    
    return data

#This function retrieves the audio features for the given list of songs using the Spotify API
def getUserSongFeatures(spotifyApiAccessor, song_ids):
    #Get the audio features for all songs in the user's library
    song_features = spotifyApiAccessor.spotifyAccessor.audio_features(song_ids)
    song_features_final_list = []

    #Get the column headers and get rid of unneeded columns
    headers = clean_data(list(song_features[0].keys()))
    song_features_final_list.append(headers)

    #Loop through the list of features to store all the needed values and drop the unneeded ones
    for features in song_features:
        features_cleaned = clean_data(list(features.values()))
        song_features_final_list.append(features_cleaned)

    with open("mysongs.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        for row in song_features_final_list:
            writer.writerow(row)

    return song_features_final_list

#This function retrieves song recommendations from the database based on the clusters it is given
def get_recommendations(clusters):
    recommendations = Song.objects.filter()

    return recommendations