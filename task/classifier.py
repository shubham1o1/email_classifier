import dataPrep
import dataProcessing
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

dataPrep.make_csv() #makes 30*30 csv file, each field represents association between keywords
dataProcessing.write_files() # find support of keywords, perform regression like operation on each key words

# Importing the dataset
dataset = pd.read_csv('pair_reg_sup.csv')
X = dataset.iloc[0:, [1, 2]].values
# print(X)
list_kw = dataset["Keywords"].tolist()


kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)


#Saving Clusters in a separate list
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
for i in range(len(y_kmeans)):
    if (y_kmeans[i]==0):
        cluster1.append(list_kw[i])
    elif (y_kmeans[i]==1):
        cluster2.append(list_kw[i])
    elif (y_kmeans[i]==2):
        cluster3.append(list_kw[i])
    elif (y_kmeans[i]==3):
        cluster4.append(list_kw[i])
    elif (y_kmeans[i]==4):
        cluster5.append(list_kw[i])


#Saving each cluster in new line of a .txt file
with open("Output.txt","w")as file :
    file.write("Cluster 1: ")
    for l in cluster1:
        file.write(l+ " ")
    file.write("\nCluster 2: ")
    for l in cluster2:
        file.write(l + " ")
    file.write("\nCluster 3: ")
    for l in cluster3:
        file.write(l + " ")
    file.write("\nCluster 4: ")
    for l in cluster4:
        file.write(l + " ")
    file.write("\nCluster 5: ")
    for l in cluster5:
        file.write(l + " ")