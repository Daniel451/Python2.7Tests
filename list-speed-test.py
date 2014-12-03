import speedtest 
import numpy

a = numpy.arange(100000)

speed = speedtest.Speedtest()

speed.record("start")

loops = 10000000

for i in range(0, loops):
    len(a)

speed.record("bla1")

for i in range(0, loops):
    a.shape[0]

speed.record("bla2")

for i in xrange(0, loops):
    a.shape[0]

speed.record("bla3")

for i in xrange(0, loops):
    len(a)

speed.record("bla3")

speed.printRecords()
