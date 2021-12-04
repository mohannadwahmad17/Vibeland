import csv
import os
from typing import final

data_file_path = "./"

files = os.listdir(data_file_path)
final1 = []
final2 = []

with open (os.path.join(data_file_path, files[1])) as csv_file:
    songs = csv.reader(csv_file)
    count = 0
    
    for song in songs:
        if len(song) == 0:
            continue
        if song[0] == "Danceability":
            continue
        
        else:
            count +=1
            final1.append(song)
    print(count)

with open (os.path.join(data_file_path, files[0])) as csv_file:
    songs = csv.reader(csv_file)
    count = 0
    
    for song in songs:

        if song[0] == "Name":
            continue

        if song[19]=="":
            continue
        else:
            count +=1
            final2.append(song)
    print(count)
count = 0
for i in range(len(final1)):
    print("index: " + str(i))
    if len(final1[i]) == len(final2[i][1:12]):
    
        if final1[i] != final2[i][1:12]:
            print("equal")
            print()
            count+=1
    else:
        print("diff lengths!")
        print(i)
        print()
print(count)