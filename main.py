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



filename = input("Nome do arquivo: ");

print("Valores de máximo e minimo:", end="")
kMax, kMin = map(int, input().split())

datalist = list()
file = open(filename, "r")
next(file)

for line in file:
	name, x, y = line.split()
	datalist.append(cls.Data(name,[float(x), float(y)]))

avgLink = avg.averageLink(datalist, kMin, kMax)
kMean = km.kMean(datalist, kMin, kMax)
sngLink = sl.singleLink(datalist, kMin, kMax)

name = filename.split('.')
name = filename[0] + ".clu"
indice_rand(kMean, name)