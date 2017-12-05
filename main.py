import cluster as cls
import kmean as km
import singlelink as sl
import averagelink as avg
from sklearn.metrics.cluster import adjusted_rand_score as rs


def indice_rand(list1, name):

	datalist = list()
	file = open(name, "r")
	next(file)

	for line in file:
		name, ind = line.split()
		datalist.append(ind)

	return rs(list1, datalist)



name = input("Nome do arquivo: ");

datalist = list()
file = open(name, "r")
next(file)

for line in file:
	name, x, y = line.split()
	datalist.append(cls.Data(name,[x,y]))

avgLink = avg.averageLink(datalist, 1, 9)
      
kMean = km.kMean(datalist, 4, 1000)

sngLink = sl.singleLink(datalist, 1, 9)

#indice_rand([0,0,0], "1.clu")