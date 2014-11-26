import speedtest 
import numpy

a = numpy.arange(100000)

speed = speedtest.Speedtest()

speed.record("start")

for i in xrange(0,100000):
    len(a)
print(len(a))

speed.record("bla1")

for i in xrange(0,100000):
    a.shape[0]
print(a.shape[0])

speed.record("bla2")

for i in xrange(0,100000):
    a.shape[0]
print(a.shape[0])

speed.record("bla3")

for i in xrange(0,100000):
    len(a)
print(len(a))

speed.record("bla3")

speed.printRecords()
