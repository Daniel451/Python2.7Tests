


from dbscan import dbscan
import numpy as np

filename = "blubb2.txt"


with open(filename) as f:
    data = f.read()

data = data.split("\n")
data = data[1:]

data = [ i.split(" ") for i in data ]


# x data
u_raw = [ i[2] for i in filter(lambda x: len(x) > 4, data) ]

# y data
v_raw = [ i[3] for i in filter(lambda x: len(x) > 4, data) ]


# set data
datax = np.array(v_raw, dtype=np.float64)
datay = np.array(u_raw, dtype=np.float64)

xmin = np.min(datax)
xmax = np.max(datax)
ymin = np.min(datay)
ymax = np.max(datay)

minPoints = 4
epsilon = 40.0

dbs = dbscan(datax, datay, minPoints, epsilon)

dbs.plot(xmin, xmax, ymin, ymax)
