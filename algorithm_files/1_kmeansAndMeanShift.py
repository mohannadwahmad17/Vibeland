from numpy import sqrt 

def distance(point, point2):
    if len(point) != len(point2):
        print("Error. Points not in same dimensionality")
        return
    else:
        length = 0
        for i in range(len(point)):
            length += (point[i] - point2[i])**2
        return(sqrt(length))

def classifier(e):
    return e['distance'];
            
import random
import copy

def kmeans_clustering(data, k, max_iter):
    centroids = []
    num_features = len(data[0])
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

from random import sample
#Mean shift clustering
def mean_shift_clustering(data, kernel_size, max_iter, num_of_windows):
    cdata = copy.deepcopy(data)
    #Start a center at every point in the data
    centers = sample(cdata,num_of_windows)
    #Seperate array to store how many points are in each cluster
    points_in_cluster = [0] * len(cdata)
    num_iters = 0
    
    #While below max number of iterations, shift the cluster centers
    while(num_iters < max_iter):
        for i in range(len(centers)):
            centers[i], points_in_cluster[i] = mean_shift(centers[i], cdata, kernel_size)
        num_iters += 1
        
        
    #Clean up cluster centers: consolidate any cluster centers that are within each other
    final_centers = []
    biggest_center = -1
    #A cluster with 0 points is a cluster that has already been addressed
    #When biggest_center is 0, all clusters have been addressed
    while(True):
        #Find center w/ most point
        biggest_center = max(points_in_cluster)
        if(biggest_center == 0):
            break
        max_index = points_in_cluster.index(biggest_center)
        final_centers.append(centers[max_index])
        #Check all centers to see if they are within kernel. 
        for j in range(len(centers)):
            #If they are, remove them from final kernel contention
            if(distance(centers[max_index], centers[j]) < kernel_size):
                #Setting points_in_cluster to 0 is "removing" cluster
                points_in_cluster[j] = 0
        points_in_cluster[max_index] = 0
    #Assign points to closest cluster center
    for i in range(len(cdata)):
        closest_dist = -1
        closest_center = -1
        j = 0
        for center in final_centers:
            dist = distance(cdata[i], center)
            if(closest_dist > dist or closest_dist == -1):
                closest_dist = dist
                closest_center = j
            j += 1
        cdata[i].append(closest_center)
    return final_centers, cdata
    
#Shift function for mean shift clustering
def mean_shift(center, data, kernel_size):
    #Declare holder to track new center
    new_center = [0] * len(center)
    #Count number of points in clusters
    points_in_cluster = 0
    
    #Loop through each point to see if they are in kernel
    for point in data:
        dist = distance(center, point)
        if(dist <= kernel_size):
            #If in kernel, add them to running total of points in cluster
            for i in range(len(new_center)):
                new_center[i] += point[i]
            points_in_cluster += 1
    
    #Average the running total for points
    for i in range(len(new_center)):
        new_center[i] /= points_in_cluster
        
    #Return new center
    return(new_center, points_in_cluster)

#Code to read in data file "data.csv"
import csv
data = []
with open('data.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            data.append(row)
            line_count += 1
print(data[0])
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = float(data[i][j])
print(data[0])


#SSE Calculation code
import copy
def SSE(data, centroids):
    #Copy data so it isn't edited
    cdata = copy.deepcopy(data)
    total_error = 0
    cluster_errors = [0] * len(centroids)
    points_per_cluster = [0] * len(centroids)
    cluster_index = len(cdata[0]) - 1
    #Get distance based off cluster its in
    for point in cdata: 
        cluster = point[cluster_index]
        point.pop(cluster_index)
        mean_error = distance(point, centroids[cluster]) ** 2
        cluster_errors[cluster] += mean_error
        total_error += mean_error
        points_per_cluster[cluster] += 1
    #Get per-cluster error
    for i in range(len(cluster_errors)):
        if(points_per_cluster[i] != 0):
            cluster_errors[i] /= points_per_cluster[i]
    #Divide by number of points
    total_error /= len(cdata)
    return(total_error, cluster_errors)
    
from matplotlib import pyplot as plt

#Run kmeans test over 60 different amounts of clusters
SSEs = []
ClusterSSEs = []
cluster_count = []
for i in range(60):
    if(i%10 == 0):
        print(i)
    kmeans_data, kmeans_centroids = kmeans_clustering(data, i + 2, 300)
    total_error, cluster_errors = SSE(kmeans_data, kmeans_centroids)
    SSEs.append(total_error)
    ClusterSSEs.append(cluster_errors)
    cluster_count.append(i+2)
print(SSEs)
plt.plot(cluster_count, SSEs)

#Run MSE test over 30 different window sizes
MSSSEs = []
MScluster_count = []
for c in range(30):
    if(c%10 == 0):
        print(c)
    MS_centroids,MS_data = mean_shift_clustering(data, 0.05 * (c+1), 200, 60)
    MStotal_error, MScluster_errors = SSE(MS_data, MS_centroids)
    MSSSEs.append(MStotal_error)
    MSClusterSSEs.append(MScluster_errors)
    MScluster_count.append((c+1) * .05)
print(MSSSEs)
plt.plot(MScluster_count, MSSSEs)

#Run final MSE run with chosen window size
final_centroids, final_data = mean_shift_clustering(data, 0.25, 200, 150)

#Function to find the closest centroid given a centroid list
def closest_centroid(centroids, input_data):
    cluster_counts = [0] * len(centroids)
    for data in input_data:
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
    for i in range(len(cluster_counts)):
        if(cluster_counts[i] > biggest_count):
            biggest_count = cluster_counts[i]
            best_cluster = i
    return(best_cluster)
    
