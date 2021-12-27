from Vibeland_api.constants.constants import CENTROIDS
from Vibeland_api.recommender.algorithms import *
from Vibeland_api.models import Song
from random import sample
import requests 
import csv

#This is the central function that calls the methods to perform the song library analysis and song recommendation process
def recommendationEngine(spotifyApiAccessor):
    #Get the current user's song library
    user_song_library, song_ids = getUserSongLibrary(spotifyApiAccessor)

    #Retrieve the audio features of each of the songs in the user's library
    user_song_features = getUserSongFeatures(spotifyApiAccessor, song_ids)

    #Scale the user song data
    scaled_user_song_features = scale_data(user_song_features)

    #Run the audio features for each song through the kmenas clustering algorithm to analyze the data
    best_cluster, second_best_cluster, third_best_cluster = closest_centroid(CENTROIDS, scaled_user_song_features)

    #Using the clusters obtained from the algorithm, query the song DB for appropriate song recommendations
    recommendations = get_recommendations(best_cluster, second_best_cluster, third_best_cluster, spotifyApiAccessor.token)

    return recommendations

#This function uses the spotify API to get the current user's song library along with extra details to be shown on the frontend
def getUserSongLibrary(spotifyApiAccessor):
    user_library = []
    song_search_limit = 50
    
    #Get the current user's saved song library
    for offset in range(0, 1000000, song_search_limit):
        user_library_response = spotifyApiAccessor.spotifyAccessor.current_user_saved_tracks(limit=song_search_limit, offset=offset)

        if len(user_library_response['items']) == 0:
            break
        user_library.append(user_library_response)

    song_ids = []
    song_tuples = []

    #Extract the relevant information from the retrieved list of song items
    for set in user_library:
        for item in set['items']:
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

#This function retrieves the audio features for the given list of songs using the Spotify API
def getUserSongFeatures(spotifyApiAccessor, song_ids):
    limit = 50
    song_features = []
    song_features_final_list = []
    
    #Get the audio features for all songs in the user's library
    for offset in range(0, len(song_ids), limit):
        song_features += spotifyApiAccessor.spotifyAccessor.audio_features(song_ids[offset:limit])

    #Get the column headers and get rid of unneeded columns
    headers = clean_data(list(song_features[0].keys()))
    song_features_final_list.append(headers)

    #Loop through the list of features to store all the needed values and drop the unneeded ones
    for features in song_features:
        #Make sure the features group is not null before proceeding
        if features != None:
            features_cleaned = clean_data(list(features.values()))
            song_features_final_list.append(features_cleaned)

    with open("mysongs.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        for row in song_features_final_list:
            writer.writerow(row)

    return song_features_final_list

#This function retrieves song recommendations from the database based on the clusters it is given
def get_recommendations(cluster1, cluster2, cluster3, access_token):
    recommendations = {}
    recommendations_final = []

    #Retrieve recommendations from the database
    rec1 = list(Song.objects.filter(centroid__iexact = cluster1).values_list())
    rec2 = list(Song.objects.filter(centroid__iexact = cluster2).values_list())
    rec3 = list(Song.objects.filter(centroid__iexact = cluster3).values_list())

    #Get samples for each of the three best clusters
    recommendations["rec1"] = sample(rec1, 5)
    recommendations["rec2"] = sample(rec2, 3)
    recommendations["rec3"] = sample(rec3, 1)

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }

    #For each recommendation, retrieve the relevant information
    for recommendation in recommendations:
        #For each of the songs, retrieve the necessary information to be displayed on the frontend
        for song in recommendations[recommendation]:
            songInfo = requests.get("https://api.spotify.com/v1/tracks/" + song[14], headers=headers)
            songInfo = songInfo.json()
            
            artistInfo = requests.get("https://api.spotify.com/v1/artists/" + songInfo['artists'][0]['id'], headers=headers)
            artistInfo = artistInfo.json()

            song_tuple = {
                "songid": songInfo['id'],
                "genre": song[20],
                "tier": recommendation,
                "title": songInfo['name'],
                "songuri": songInfo['uri'],
                "songprev": songInfo['preview_url'],
                "artists": songInfo['artists'][0]['name'],
                "songurl": songInfo['external_urls']['spotify'],
                "coverart": songInfo['album']['images'][0]['url'],
            }
            
            if len(artistInfo['images']) > 0:
                song_tuple["artistImage"] = artistInfo['images'][0]['url']
            
            recommendations_final.append(song_tuple)

    return recommendations_final

#Remove the unneeded audio features from the data
def clean_data(data):
    del(data[11:18])
    del(data[6])
    del(data[3])
    
    return data