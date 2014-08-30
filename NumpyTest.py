import numpy
import time


time1 = time.time()

print(str(324.2314 - 126.92158))

time2 = time.time()

print("Zeit: " + str(time2-time1))


time3 = time.time()

print(str(numpy.array([324.2314]) - numpy.array([126.92158])))

time4 = time.time()

print("Zeit: " + str(time4-time3))
