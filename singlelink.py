from copy import deepcopy
import numpy as np
import cluster as cls

d = [cls.Data('Homer', [0.0, 250.0, 36.0]),
     cls.Data('Marge', [10.0, 150.0, 34.0]),
     cls.Data('Bart', [2.0, 90.0, 10.0]),
     cls.Data('Lisa', [6.0, 78.0, 8.0]),
     cls.Data('Maggie', [4.0, 20.0, 1.0]),
     cls.Data('Abe', [1.0, 170.0, 70.0]),
     cls.Data('Selma', [8.0, 160.0, 41.0]),
     cls.Data('Otto', [10.0, 180.0, 38.0]),
     cls.Data('Krusty', [6.0, 200.0, 45.0])]   

distMatrix = list()
distList = list()

# Calcula distância todos pra todos
def calculateDistance(dataset):
    global distMatrix
    global distList
    for i in range(0, len(dataset)):
        line = list()
        for j in range(i, len(dataset)):
            dist = cls.euclidianDistance(dataset[i].features, dataset[j].features)
            if (i != j):
                distList += [[i, j, dist]]
            line.append(dist)
        distMatrix.append(line)        
    distList.sort(key=lambda x : x[2]) 
    
    
def singleLink(dataset, kMin, kMax):    
    global distMatrix
    global distList
    
    # Cortes do dendrograma
    dendrogram = list()
    
    # Inicializa N clusters
    clusterSet = cls.ClusterSet(dataset)
    calculateDistance(dataset)    
        
    # Itera até encotrar os cortes desejados
    while (clusterSet.numClusters() >= kMin):
        if (clusterSet.numClusters() <= kMax):
            dendrogram.append(deepcopy(clusterSet))
            if (clusterSet.numClusters() == kMin):                
                break
            
        # Junta clusters mais próximos    
        a, b = distList[0][0], distList[0][1]                     
        clusterSet.mergeClusters(a, b)             
        
        # Remove as distancias dos clusters que juntamos e atualiza a posicao dos seguintes
        for i in range(len(distList)-1, -1, -1):
            if (distList[i][0] == a or distList[i][1] == a or 
                distList[i][0] == b or distList[i][1] == b):
                distList.pop(i)
            else: 
                if (distList[i][0] > b):
                    distList[i][0] -= 1
                if (distList[i][1] > b):
                    distList[i][1] -= 1                
                
        # Atualiza as distancias            
        for i in range(0, len(distMatrix)):                         
            if (i < a):
                distMatrix[i][a-i] = min(distMatrix[i][a-i], distMatrix[i][b-i])
                distList += [[i, a, distMatrix[i][a-i]]]
            elif (i > a and i < b):
                distMatrix[a][i-a] = min(distMatrix[a][i-a], distMatrix[i][b-i])
                distList += [[a, i, distMatrix[a][i-a]]]
            elif (i > b):
                distMatrix[a][i-a] = min(distMatrix[a][i-a], distMatrix[b][i-b])                
                distList += [[a, i-1, distMatrix[a][i-a]]]                                  
        
        # Remove a linha e coluna do cluster agrupado da matriz
        distMatrix.pop(b)
        pos = b - len(distMatrix[0])
        for line in distMatrix[:b]:
            line.pop(pos)            
        
        # Ordena a lista de distancia
        distList.sort(key=lambda x : x[2])
                
    return dendrogram
    
    
clst = singleLink(d, 1, 9)
for c in clst:
    c.printId()
    print()