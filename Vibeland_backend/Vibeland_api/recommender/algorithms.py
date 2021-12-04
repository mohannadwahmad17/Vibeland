import csv
import copy
import random
from math import sqrt

#Compute the euclidean distance between the given points
def distance(point, point2):
    if len(point) != len(point2):
        print("Error. Points not in same dimensionality")
        return
    else:
        length = 0
        for i in range(len(point)):
            length += (point[i] - point2[i])**2
        return(sqrt(length))

def kmeans_clustering(data, k, max_iter):
    centroids = []
    num_features = len(data[0])
    print(data[0][0])
    for i in range(k):
        centroid = []
        for feature in data[0]:
            centroid.append(random.random())
        centroids.append(centroid)

    old_centroids = []
    for datapoint in data:
        datapoint.append(0)
    iters = 0
    while(iters < max_iter and centroids != old_centroids):
        
        #Keep old centroids for stopping point purposes
        old_centroids = copy.deepcopy(centroids)
        #Find new clusters for every point
        for dataPoint in data:
            dists = []
            for centroid in centroids:
                dists.append(0.0)
            i = 0
            for feature in dataPoint:
                #Don't include cluster in loop
                if(i >= num_features):
                    break
                j = 0
                for centroid in centroids:
                    #Uses Euclidean distance
                    dists[j] += (feature - centroid[i]) ** 2
                    j += 1
                i += 1
            shortestDist = 99999999999999999999999999999999999999999

            for i in range(len(dists)):
                if(dists[i] < shortestDist):
                    shortestDist = dists[i]
                    dataPoint[num_features] = i
        #Update centroids
        for i in range(len(centroids)):
            points_in_cluster = 0
            for j in range(len(centroids[i])):
                centroids[i][j] = 0
            #Check if datapoint is in centroid: if so, add to running total
            for dataPoint in data:
                if dataPoint[num_features] == i:
                    points_in_cluster += 1
                    for j in range(len(centroids[i])):
                        centroids[i][j] += dataPoint[j]
            if points_in_cluster == 0:
                for j in range(len(centroids[i])):
                    centroids[i][j] = random.random()
            #Divide by number of points in centroid
            else:
                for j in range(len(centroids[i])):
                    centroids[i][j] = centroids[i][j]/points_in_cluster

        iters+=1
    return(data, centroids)

#This function performs the classification of the given user's songs based on the given centroids
def closest_centroid(centroids, input_data):
    cluster_counts = [0] * len(centroids)
    for data in input_data:
        if data[0] == "danceability":
            continue

        closest_dist = -1
        closest_center = -1
        j = 0
        for center in centroids:
            dist = distance(data, center)
            if(closest_dist > dist or closest_dist == -1):
                closest_dist = dist
                closest_center = j
            j += 1
        cluster_counts[closest_center] += 1
    
    biggest_count = -1
    best_cluster = -1
    second_best_cluster = -1
    third_best_cluster = -1
    for i in range(len(cluster_counts)):
        if(cluster_counts[i] > biggest_count):
            biggest_count = cluster_counts[i]
            best_cluster = i

    biggest_count = -1        
    for i in range(len(cluster_counts)):
        if(cluster_counts[i] > biggest_count) and i != best_cluster:
            biggest_count = cluster_counts[i]
            second_best_cluster = i
    
    biggest_count = -1        
    for i in range(len(cluster_counts)):
        if(cluster_counts[i] > biggest_count) and i != second_best_cluster and i != third_best_cluster:
            biggest_count = cluster_counts[i]
            third_best_cluster = i

    return best_cluster, second_best_cluster, third_best_cluster


def scale_data(data):
    scalars = [[0.0, 0.988], [0.0, 1.0], [0,11], [0,1], [0.0,0.966], [0.0, 0.999], [0.0, 1.0], [0.0, 1.0], [0.0, 248.066]]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = (data[i][j] - scalars[j][0]) / (scalars[j][1] - scalars[j][0])
    return(data)