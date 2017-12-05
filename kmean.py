from random import randint
from copy import deepcopy
import numpy as np
import cluster as cls

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
