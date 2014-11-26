import speedtest 


size = 10000
A = []
for i in range(0,size):
   A.append(i)
B = list(A)


speed = speedtest.Speedtest()

speed.record("start")

C = []
D = []
for aitem in A:
   C.append(aitem+1)
   for bitem in B:
      D.append(bitem+1)

speed.record("for rdy")

C = [
      item+1 for item in A
   ]

D = [
      bitem+1 for bitem in B for aitem in A
   ]

speed.record("list rdy")

speed.printRecords()
