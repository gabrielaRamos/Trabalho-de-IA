import numpy as np

# Calcula a distancia euclidiana entre duas listas de coordenadas
def euclidianDistance(a, b):
    return np.linalg.norm(np.array(a)-np.array(b))

# Classe para um dado
class Data:
    # Parametros --> dado individual com id e [features]
    def __init__(self, id, features):
        self.id = id
        self.features = features

    # Compara dois dados
    def __eq__(self, other):
        return self.id == other.id


# Classe para um cluster individual
class Cluster:
    # Parametros --> Lista de dados
    def __init__(self, dataset):
        self.dataset = dataset
        self.centroid = None
        self.updateCentroid()
        
    # Parametros --> Data
    # Adiciona o dado no cluster    
    def add(self, data):
        for i in range(0, len(self.dataset)):
            if (self.dataset[i].id == data.id):
                return
            if (self.dataset[i].id > data.id):
                self.dataset.insert(i, data)
                return
        self.dataset.append(data)                
        
    # Atualiza o centroid do cluster
    def updateCentroid(self):
        self.centroid = np.average([i.features for i in self.dataset], 0).tolist()
    
    # Limpa os dados do cluster (mas mantem o centroid)
    def clean(self):
        self.dataset = list()
    
    # Compara dois clusters
    def __eq__(self, other):
        return self.dataset == other.dataset
        
    # Exibe o cluster com todos os dados
    def printAll(self):
        for i, d in enumerate(self.dataset):
            if i != 0:
                print(', ', end='')
            print(d.id + ':' + str(d.features), end='')
    
    # Exibe o cluster com os ids
    def printId(self):
        for i, d in enumerate(self.dataset):
            if i != 0:
                print(', ', end='')
            print(d.id, end='')
            
            
            
# Classe para um conjunto de clusters
class ClusterSet:
    # Parametros --> Lista de dados
    def __init__(self, dataset):
        self.clusters = list()
        for d in dataset:
            self.clusters.append(Cluster([d]))            
            
    # Clusteriza pelo centroid mais proximo
    # Parametros --> Dado
    def clusterizeByCentroid(self, data):        
        minDist = euclidianDistance(data.features, self.clusters[0].centroid)
        clusterIndex = 0
        for i, c in enumerate(self.clusters[1:]):
            if (euclidianDistance(data.features, c.centroid) < minDist):
                minDist = euclidianDistance(data.features, c.centroid)
                clusterIndex = i+1    
        self.clusters[clusterIndex].add(data)          
        
    # Limpa os clusters
    def clean(self):
        for c in self.clusters:
            c.clean()
            
    # Atualiza os centroids
    def updateCentroids(self):
        for c in self.clusters:
            c.updateCentroid()
            
    # Combina dois clusters
    def mergeClusters(self, c1, c2):
        for data in self.clusters[c2].dataset:
            self.clusters[c1].add(data)
        self.clusters.pop(c2)
    
    # Compara dois clusterset
    def __eq__(self, other):        
        return self.clusters == other.clusters
            
    # Ordena um cluster
    def sortCluster(self):
        self.clusters.sort(key=lambda x: x.dataset[0].id)
    
    # Retorna numero de clusters
    def numClusters(self):
        return len(self.clusters)
    
    # Calcular a media de todos pra todos entre dois clusters
    def averageDistCluster(self, c1, c2):
        dist = 0.0        
        for d1 in self.clusters[c1].dataset:
            for d2 in self.clusters[c2].dataset:
                dist += euclidianDistance(d1.features, d2.features)
        return dist/((len(self.clusters[c1].dataset)*len(self.clusters[c2].dataset)))
    
    # Exibe os clusters com todos os dados
    def printAll(self):        
        for i, c in enumerate(self.clusters):
            print('Cluster ' + str(i+1) + '=> ', end='')
            c.printAll()
            print()
    
    # Exibe os clusters com os ids
    def printId(self):        
        for i, c in enumerate(self.clusters):
            print('Cluster ' + str(i+1) + ' => ', end='')
            c.printId()
            print()
        