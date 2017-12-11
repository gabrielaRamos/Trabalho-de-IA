import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
data = np.array([[4.29488806,-5.34487081],
                [3.63116248,-2.48616998],
                [-0.56023222,-5.89586997],
                [-0.51538502,-2.62569576],
                [-4.08561754,-4.2870525 ],
                [-0.80869722,10.12529582]])
colors = ['red','red','red','blue','red','blue']
for xy, color in zip(data, colors):
    ax.plot(xy[0],xy[1],'o',color=color, picker=True)

plt.show()