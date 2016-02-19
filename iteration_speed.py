import timeit
import time
import random

xs = range(0, 1000000)


def for1(xs):
    for item in xs:
        return item + 1

# uncommented: ultra slow!!
# def for2(xs):
#     for i in range(len(xs)):
#         return xs[i] + 1

def for3(xs):
    for i in xrange(len(xs)):
        return xs[i] + 1

def for4(xs):
    it = iter(xrange(len(xs)))
    for i in it:
        return xs[i] + 1

def gen5(n):
    i = 0
    while i < n:
        yield i
        i += 1

def for5(xs):
    for i in gen5(len(xs)):
        return xs[i] + 1

def for6(xs):
    for key, val in enumerate(xs):
        return xs[key] + 1

def for7(xs):
    for key, val in enumerate(xs):
        return val + 1


N = 1000000
results = []

time.sleep(0.1)
results.append(
        ("for1:", timeit.timeit("for1(xs)", "from __main__ import for1, xs", number=N))
)


# uncommented: ultra slow!!
# time.sleep(0.1)
# results.append(
#         ("for2:", timeit.timeit("for2(xs)", "from __main__ import for2, xs", number=N))
# )

time.sleep(0.1)
results.append(
        ("for3:", timeit.timeit("for3(xs)", "from __main__ import for3, xs", number=N))
)

time.sleep(0.1)
results.append(
        ("for4:", timeit.timeit("for4(xs)", "from __main__ import for4, xs", number=N))
)

time.sleep(0.1)
results.append(
        ("for5:", timeit.timeit("for5(xs)", "from __main__ import for5, xs", number=N))
)

time.sleep(0.1)
results.append(
        ("for6:", timeit.timeit("for6(xs)", "from __main__ import for6, xs", number=N))
)

time.sleep(0.1)
results.append(
        ("for7:", timeit.timeit("for7(xs)", "from __main__ import for7, xs", number=N))
)


for item in sorted(results, key=lambda x: x[1]):
    print(item)