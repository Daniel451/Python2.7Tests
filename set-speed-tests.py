import numpy as np
import timeit


SIZES = [100, 1000, 10000, 100000, 1000000]
a = dict()
b = dict()

def populate_dict(d):
    global SIZES
    for num in SIZES:
        d["np" + str(num)] = np.unique(np.random.randint(0, high=num, size=num))
        d["py" + str(num)] = set(d["np" + str(num)])

populate_dict(a)
populate_dict(b)

t = dict()

t["np100"] = timeit.timeit("np.intersect1d(a['np100'], b['np100'])", setup="from __main__ import a, b, np", number=1000)
t["np1000"] = timeit.timeit("np.intersect1d(a['np1000'], b['np1000'])", setup="from __main__ import a, b, np", number=1000)
t["np10000"] = timeit.timeit("np.intersect1d(a['np10000'], b['np10000'])", setup="from __main__ import a, b, np", number=1000)
t["np100000"] = timeit.timeit("np.intersect1d(a['np100000'], b['np100000'])", setup="from __main__ import a, b, np", number=1000)
t["np1000000"] = timeit.timeit("np.intersect1d(a['np1000000'], b['np1000000'])", setup="from __main__ import a, b, np", number=100)

t["py100"] = timeit.timeit("a['py100'].intersection(b['py100'])", setup="from __main__ import a, b", number=1000)
t["py1000"] = timeit.timeit("a['py1000'].intersection(b['py1000'])", setup="from __main__ import a, b", number=1000)
t["py10000"] = timeit.timeit("a['py10000'].intersection(b['py10000'])", setup="from __main__ import a, b", number=1000)
t["py100000"] = timeit.timeit("a['py100000'].intersection(b['py100000'])", setup="from __main__ import a, b", number=1000)
t["py1000000"] = timeit.timeit("a['py1000000'].intersection(b['py1000000'])", setup="from __main__ import a, b", number=100)

def rel_diff(num_a, num_b):
    return (100.0 / num_a) * num_b

for num in SIZES:
    tpy = t["py"+str(num)]
    tnp = t["np"+str(num)]
    print("[py{0: <7}]  {1: >10.6f}  <-[{3:.2f}%]->  {2: >10.6f}  [np{0: <7}]".format(num, tpy, tnp, rel_diff(tpy, tnp)))
