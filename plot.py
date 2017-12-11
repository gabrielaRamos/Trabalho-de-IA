import numpy as np
import matplotlib.pyplot as plt

cm1 = ['red', 'blue']
cm2 = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan', 'pink']

for dataset in ['c2ds1-2sp', 'c2ds3-2g', 'monkey']:    
    datalist = list()
    with open("datasets/" + dataset + ".txt", "r") as f:
        next(f)    
        for line in f:
            name, x, y = line.split()
            datalist.append([float(x), float(y)])
        data = np.asarray(datalist)            
    
    for alg in ['kMean', 'avgLink', 'sngLink']:
        fig, ax = plt.subplots()                
        clusterid = {}
        if (dataset == 'monkey'):
            num = '8'
        else:
            num = '2'        
        
        with open('results/' + alg + '_' + dataset + '_' + num + '.clu', "r") as f:                 
            for line in f:
                name, ind = line.split()
                clusterid[name] =int(ind)        
        colors = []
        with open("datasets/" + dataset + ".txt", "r") as f:
            next(f)    
            for line in f:
                name, x, y = line.split()
                if (dataset == 'monkey'):        
                    colors.append(cm2[clusterid[name]-1])
                else:
                    colors.append(cm1[clusterid[name]])
                    
        for xy, color in zip(data, colors):
            ax.plot(xy[0],xy[1],'o',color=color, picker=True)
        
        plt.savefig(alg + '_' + dataset + '.png')