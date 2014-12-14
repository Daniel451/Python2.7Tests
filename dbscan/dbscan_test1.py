# -*- coding: utf-8 -*-



from dbscan import dbscan
import numpy as np


size = 6.0 * np.pi
steps = size / 200.0

originaly = np.sin(np.arange(0.0, size, steps)) * 80.0
originalx = np.arange(-140.0, 140.0, 280.0 / len(originaly) ) 

noise_factor = 20.0
noisey = np.random.uniform(-noise_factor, noise_factor, len(originaly))
noisex = np.random.uniform(-noise_factor, noise_factor, len(originalx))

datax = originalx + noisex
datay = originaly + noisey

minPoints = 3
epsilon = 10.0

dbs = dbscan(datax, datay, minPoints, epsilon)

dbs.plot(-160, 160, -140, 140)


#steps = 4
#datax2 = np.arange(-150,150,steps)
#datay2 = np.sin(np.arange(-150,150,steps)/25.0) * 100.0

#dbs2 = dbscan(datax2, datay2, 3, 15.0)
#dbs2.plot()
