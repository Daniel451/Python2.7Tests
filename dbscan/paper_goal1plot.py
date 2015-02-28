

import numpy as np
import random
from matplotlib.pylab import *

filename = "tamara_cali_u2000.log"


with open(filename) as f:
    data = f.read()

data = data.split("\n")

#data = filter(lambda(key,val): False if key % 2 == 0 else True, enumerate(data))
data = [ i.replace("nan", "0").split(" ") for i in data ]
print data[1]

#print(data[0:10])

# ufiltered data
u_filtered = [ i[7] for i in filter(lambda x: len(x) > 4, data) ]
# vfiltered data
v_filtered = [ i[8] for i in filter(lambda x: len(x) > 4, data) ]

# ufiltered data
u_raw = [ i[1] for i in filter(lambda x: len(x) > 4, data) ]
# vfiltered data
v_raw = [ i[2] for i in filter(lambda x: len(x) > 4, data) ]

def normalizer(bufferobj, offset=0.0):
    for key, val in enumerate(bufferobj):
        bufferobj[key] = val + offset
    return bufferobj

def noiser(bufferobj, low=1.0, high=1.2):
    for key, val in enumerate(bufferobj):
        bufferobj[key] = val * np.random.uniform(low, high)
    return bufferobj


# set data
datau = np.array(u_filtered[230:331], dtype=np.float64)
datav = np.array(v_filtered[230:331], dtype=np.float64)
datarawu = np.array(u_raw[230:331], dtype=np.float64)
datarawv = np.array(v_raw[230:331], dtype=np.float64)

#datau = noiser(datau, 0.9, 1.0)

#datarawu = noiser(datarawu, 5.0, 5.0)
#datarawv = noiser(datarawv, 0.97, 5.0)
#datau = noiser(datau, 4.0, 4.0)
#datav = noiser(datav, 4.0, 4.0)

datarawu = normalizer(datarawu, 200.0)
datarawv = normalizer(datarawv, 0.0)
datau = normalizer(datau, 200.0)
datav = normalizer(datav, 0.0)


print(datau[0:50])



def plot(datau, datav, datarawu, datarawv):

    # filtered
    plt.subplot()
    plt.title("goal post data")
    #    plt.ylim([ymin, ymax])
    #   plt.xlim([xmin, xmax])

    plt.xlabel("u in mm")
    plt.ylabel("v in mm")

    plt.plot(datarawu, datarawv, color="r", marker="o", linestyle="None", label="raw data")
    plt.plot(datau, datav, color="b", marker="o", linestyle="None", label="filtered, averaged data")

    plt.xticks(np.arange(0, max(datarawv)+1.0, 10.0))
    plt.yticks(np.arange(0, max(datarawu)+1.0, 10.0))

    plt.legend(loc="upper right")

    plt.show()


# plotten
plot(datav, datau, datarawv, datarawu)
