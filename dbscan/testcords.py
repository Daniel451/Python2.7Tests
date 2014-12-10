



from dbscan import dbscan
import numpy as np


# coord container
cc = list()
cc[0] = list()
cc[1] = list()

# p1 (10,10)
cc[0].append(10)
cc[1].append(10)

# p2 (10,20)
cc[0].append(10)
cc[1].append(20)

# p3 (20,10)
cc[0].append(20)
cc[1].append(10)

# p4 (20,20)
cc[0].append(20)
cc[1].append(20)

# p5 (30,30)
cc[0].append(30)
cc[1].append(30)

# p6 (40,40)
cc[0].append(40)
cc[1].append(40)

coords = numpy.array(cc)


minPoints = 2
epsilon = 10


