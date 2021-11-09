import os
import re
import csv
from Vibeland_api.models import *


def run():
    data_file_path = "Vibeland_api/data_files"

    files = os.listdir(data_file_path)

    for file in files:
        table_name = re.findall(r"(.*)Db.csv", file)[0]

        with open(os.path.join(data_file_path, file)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:

                if table_name == "song":
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
                    id=row[12],
                    uri=row[13],
                    ref_track=row[14],
                    url_features=row[15],
                    duration=row[16],
                    time_signature=row[17],
                    genre=row[18]
                )
