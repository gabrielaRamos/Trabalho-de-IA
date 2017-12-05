from random import randint
from copy import deepcopy
import numpy as np
import cluster as cls

d = [cls.Data('1', [1.0,1.0]),
     cls.Data('2', [1.5,2.0]),
     cls.Data('3', [3.0,4.0]),
     cls.Data('4', [5.0,7.0]),
     cls.Data('5', [3.5,5.0]),
     cls.Data('6', [4.5,5.0]),
     cls.Data('7', [3.5,4.5])]

# Seleciona k centroides aleatorios baseados nos objetos
def randomizeClusters(datasetLen, k):
    initialIndexes = list()
    while(len(initialIndexes) != k):
        n = randint(0, datasetLen-1)
        if n not in initialIndexes:
            initialIndexes.append(n)
    return initialIndexes


# Algoritmo de k-media que retorna lista de clusters
def kMean(dataset, k, maxIter):    
    # Inicializa os centroides
    initialClusters = list()
    for i in randomizeClusters(len(dataset), k):        
        initialClusters.append(dataset[i])
    
    # Inicializa clusterset  
    clusterset = cls.ClusterSet(initialClusters)
    previousClusterset = cls.ClusterSet([])
    
    # Verifica o critério de parada
    while (maxIter > 0):
        # Itera sobre todos os dados e associa ao cluster
        for data in dataset:
            clusterset.clusterizeByCentroid(data)
        clusterset.sortCluster()        
        # Verifica se houve mudanca nos clusters
        if (previousClusterset == clusterset):             
            return clusterset                
        previousClusterset = deepcopy(clusterset)            
        # Recalcula os centroides                
        clusterset.updateCentroids()    
        # Limpa os clusters para reagrupar
        clusterset.clean()        
        # Reduz a contagem de iteracoes
        maxIter -= 1
        
    return previousClusterset

# Main       
kMean(d, 4, 1000).printId()
