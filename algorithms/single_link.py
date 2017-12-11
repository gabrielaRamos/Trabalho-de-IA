from copy import deepcopy
from .utils import cluster as cl
from .utils import union_find as uf 

distList = list()

# Calcula distância todos pra todos
def calculateDistance(dataset):
    global distList
    for i in range(0, len(dataset)):
        for j in range(i+1, len(dataset)):            
            distList += [[i, j, cl.euclidianDistance(dataset[i].features, dataset[j].features)]]
    distList.sort(key=lambda x : x[2])     
    
def singleLink(dataset, kMin, kMax):    
    global distList
    
    # Cortes do dendrograma
    dendrogram = list()
    
    # Inicializa N clusters
    clusterSet = cl.ClusterSet(dataset)
    calculateDistance(dataset)    
    unionSet = uf.UnionFind(len(dataset))
        
    # Itera até encotrar os cortes desejados    
    while (clusterSet.numClusters >= kMin):
        if (clusterSet.numClusters <= kMax):
            dendrogram.append(deepcopy(clusterSet.cleaned()))
            if (clusterSet.numClusters == kMin):                
                break
            
        # Junta clusters mais próximos       
        while True:
            a, b = distList[0][0], distList[0][1]            
            c = unionSet.union(a, b)            
            if c[0] != -1:                
                clusterSet.mergeClusters(c[0], c[1], False)            
                distList.pop(0)
                break
            distList.pop(0)
        
    return dendrogram    