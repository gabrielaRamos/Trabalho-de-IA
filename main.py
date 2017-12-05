import cluster as cls
import kmean as km
import singlelink as sl
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
file = open(filename, "r")
next(file)

for line in file:
	name, x, y = line.split()
	datalist.append(cls.Data(name,[x,y]))


indice_rand([0,0,0], "1.clu")