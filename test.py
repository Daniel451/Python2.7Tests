from collections import namedtuple

nm = namedtuple("nm",("a","b","c"))

blubb = nm(a=1, b=2, c=3)

for item in blubb:
   print item
