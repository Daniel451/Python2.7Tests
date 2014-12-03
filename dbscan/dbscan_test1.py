# -*- coding: utf-8 -*-



from dbscan import dbscan
import numpy as np


size = 100.0

originalx = np.sin(np.arange(size)/5.0) * 100.0
originaly = np.sin(np.arange(size)/5.0) * 100.0

noisex = np.random.uniform(-50.0, 50.0, size)
noisey = np.random.uniform(-50.0, 50.0, size)

datax = originalx + noisex
datay = originaly + noisey

minPoints = 3
epsilon = 10.0

dbs = dbscan(datax, datay, minPoints, epsilon)

dbs.plot()
