


from dbscan import dbscan
import numpy as np
from matplotlib.pylab import *

filename = "GoalDBScan2.5m.txt"


with open(filename) as f:
    data = f.read()

data = data.split("\n")

data = filter(lambda(key,val): False if key % 2 == 0 else True, enumerate(data))

data = [ i[1].replace("nan", "0").split(" ") for i in data ]

print(data[0:10])

# ufiltered data
u_filtered = [ i[8] for i in filter(lambda x: len(x) > 4, data) ]
# vfiltered data
v_filtered = [ i[9] for i in filter(lambda x: len(x) > 4, data) ]

# ufiltered data
u_raw = [ i[10] for i in filter(lambda x: len(x) > 4, data) ]
# vfiltered data
v_raw = [ i[11] for i in filter(lambda x: len(x) > 4, data) ]

# set data
datau = np.array(u_filtered, dtype=np.float64)
datav = np.array(v_filtered, dtype=np.float64)
datarawu = np.array(u_raw, dtype=np.float64)
datarawv = np.array(v_raw, dtype=np.float64)

#print(datau[0:50])



def plot(datau, datav, datarawu, datarawv):

    # filtered
    plt.subplot()
    plt.title("filtered")
    #    plt.ylim([ymin, ymax])
    #   plt.xlim([xmin, xmax])
    plt.plot(datau, datav, color="b", marker="o", linestyle="None")
    plt.plot(datarawu, datarawv, color="r", marker="o", linestyle="None")

    plt.show()


# plotten
plot(datav, datau, datarawv, datarawu)
