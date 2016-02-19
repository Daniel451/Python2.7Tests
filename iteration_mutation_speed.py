from itertools import imap
import timeit
import time
import random


xs1 = range(0, 100000)
xs2 = range(0, 100000)
xs3 = range(0, 100000)
xs4 = range(0, 100000)
xs5 = range(0, 100000)


def for1(xs):
    for key in xrange(len(xs)):
        xs[key] += 1


def for2(xs):
    for key, val in enumerate(xs):
        xs[key] += 1


def for3(xs):
    xs = [e + 1 for e in xs]


def for4(xs):
    xs = map(lambda x: x + 1, xs)


def for5(xs):
    xs = list(imap(lambda x: x + 1, xs))


N = 100
results = []

time.sleep(0.1)
results.append(
        ("for1:", timeit.timeit("for1(xs1)", "from __main__ import for1, xs1", number=N))
)

time.sleep(0.1)
results.append(
        ("for2:", timeit.timeit("for2(xs2)", "from __main__ import for2, xs2", number=N))
)

time.sleep(0.1)
results.append(
        ("for3:", timeit.timeit("for3(xs3)", "from __main__ import for3, xs3", number=N))
)

time.sleep(0.1)
results.append(
        ("for4:", timeit.timeit("for4(xs4)", "from __main__ import for4, xs4", number=N))
)

time.sleep(0.1)
results.append(
        ("for5:", timeit.timeit("for5(xs5)", "from __main__ import for5, xs5", number=N))
)

for item in sorted(results, key=lambda x: x[1]):
    print(item)
