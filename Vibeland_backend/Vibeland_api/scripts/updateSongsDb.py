import os
import re
import csv
from Vibeland_api.models import *

#This function will be run to populate the database with the songs from the csv file containing all the songs
def run():
    data_file_path = "Vibeland_api/data_files"

    files = os.listdir(data_file_path)

    for file in files:
        table_name = re.findall(r"(.*)Db.csv", file)[0]

        #Open the csv file to read all the data and update the database with all the song entries
        with open(os.path.join(data_file_path, file), encoding='Latin-1') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            
            #Extract the necessary data from each row to insert all the song entries in the database
            for row in csv_reader:

                if table_name == "songs":
                    if row[0] == "Name":
                        continue

                    object, created = Song.objects.update_or_create(
                        name=row[0],
                        danceability=row[1],
                        energy=row[2],
                        key=row[3],
                        loudness=row[4],
                        mode=row[5],
                        speechness=row[6],
                        acousticness=row[7],
                        instrumentalness=row[8],
                        liveness=row[9],
                        valence=row[10],
                        tempo=row[11],
                        type=row[12],
                        trackid=row[13],
                        uri=row[14],
                        ref_track=row[15],
                        url_features=row[16],
                        duration=row[17],
                        time_signature=row[18],
                        genre=row[19],
                        centroid=row[20]
                    )

