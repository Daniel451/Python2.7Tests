


from dbscan import dbscan
import numpy as np
from matplotlib.pylab import *

filename = "GoalDBScan2.txt"


with open(filename) as f:
    data = f.read()

data = data.split("\n")

data = filter(lambda(key,val): False if key % 2 == 0 else True, enumerate(data))

data = [ i[1].replace("nan", "0").split(" ") for i in data ]

print(data[0:10])

# u data
u_raw = [ i[8] for i in filter(lambda x: len(x) > 4, data) ]

# v data
v_raw = [ i[9] for i in filter(lambda x: len(x) > 4, data) ]


# set data
datau = np.array(v_raw, dtype=np.float64)
datav = np.array(u_raw, dtype=np.float64)

#print(datau[0:50])


xmin = np.min(datau)
xmax = np.max(datau)
ymin = np.min(datav)
ymax = np.max(datav)




def plot(xdatau, datav, xmin=-150, xmax=150, ymin=-150, ymax=150):

    # filtered
    plt.subplot()
    plt.title("filtered")
    plt.ylim([ymin, ymax])
    plt.xlim([xmin, xmax])
    plt.plot(datau, datav, color="b", marker="o", linestyle="None")

    plt.show()


# plotten
plot(datau, datav, xmin, xmax, ymin, ymax)
