import csv
import copy
import random

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