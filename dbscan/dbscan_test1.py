# -*- coding: utf-8 -*-



from dbscan import dbscan
import numpy as np


size = 100.0

originalx = np.sin(np.arange(0,size,0.3)/5.0) * 100.0
originaly = np.sin(np.arange(0,size,0.3)/5.0) * 100.0

noisex = np.random.uniform(-100.0, 100.0, len(originalx))
noisey = np.random.uniform(-100.0, 100.0, len(originaly))

datax = originalx + noisex
datay = originaly + noisey

minPoints = 3
epsilon = 10.0

dbs = dbscan(datax, datay, minPoints, epsilon)

dbs.plot()


steps = 4
datax2 = np.arange(-150,150,steps)
datay2 = np.sin(np.arange(-150,150,steps)/25.0) * 100.0

dbs2 = dbscan(datax2, datay2, 3, 15.0)
dbs2.plot()
