from algorithms.utils import cluster as cl
from algorithms import single_link as sl
from algorithms import average_link as al
from algorithms import k_mean as km
from sklearn.metrics.cluster import adjusted_rand_score as rs


def indice_rand(list1, name):
    datalist = list()
    file = open(name, "r")    
    for line in file:
        name, ind = line.split()
        datalist.append(ind)    
    return rs(list1, datalist)


randFile = open("rand-index.txt", "a")
for dataset in [('c2ds1-2sp', 2, 5), ('c2ds3-2g', 2, 5), ('monkey', 5, 12)]:
    print("Lendo dataset " + dataset[0] + "...")
    datalist = list()
    file = open("datasets/" + dataset[0] + ".txt", "r")
    next(file)    
    
    for line in file:
    	name, x, y = line.split()
    	datalist.append(cl.Data(name,[float(x), float(y)]))
    
    print("Executando o algoritmo K-médias...")
    kMean = list()
    for i in range(dataset[1], dataset[2]+1):
        kMean += [km.kMean(datalist, i, 50)]        
    for clusterSet in kMean:
        clusterSet.writeToFile('results/kMean_' + dataset[0] + '_' + str(clusterSet.numClusters) + '.clu')        
        randFile.write('kMean_' + dataset[0] + '_' 
                       + str(clusterSet.numClusters) + ' -> ' 
                       +  str(indice_rand(clusterSet.listFormat(), 'datasets/' + dataset[0] + 'Real.clu')) + '\n')    
    randFile.flush()
        
    print("Executando o algoritmo Single Link...")
    sngLink = sl.singleLink(datalist, dataset[1], dataset[2])
    for clusterSet in sngLink:
        clusterSet.writeToFile('results/sngLink_' + dataset[0] + '_' + str(clusterSet.numClusters) + '.clu')
        randFile.write('sngLink' + dataset[0] + '_' 
                       + str(clusterSet.numClusters) + ' -> ' 
                       +  str(indice_rand(clusterSet.listFormat(), 'datasets/' + dataset[0] + 'Real.clu')) + '\n')
    randFile.flush()
        
    print("Executando o algoritmo Average Link...")
    avgLink = al.averageLink(datalist, dataset[1], dataset[2])
    for clusterSet in avgLink:
        clusterSet.writeToFile('results/avgLink_' + dataset[0] + '_' + str(clusterSet.numClusters) + '.clu')        
        randFile.write('avgLink' + dataset[0] + '_' 
                       + str(clusterSet.numClusters) + ' -> ' 
                       +  str(indice_rand(clusterSet.listFormat(), 'datasets/' + dataset[0] + 'Real.clu')) + '\n')
    randFile.flush()
    file.close()    
randFile.close()