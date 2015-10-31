import multiprocessing
import numpy as np
import timeit
import time


lst = list(np.random.randint(1, 100, 100000))
loops = 1000

def sum_for(xs):
    sum = 0
    for elem in xs:
        sum += elem
    return sum

def sum_for_range(xs):
    sum = 0
    for elem in range(0, len(xs)):
        sum += elem
    return sum

def sum_for_xrange(xs):
    sum = 0
    for elem in xrange(0, len(xs)):
        sum += elem
    return sum

def sum_for_numpy(xs):
    sum = 0
    xs = np.array(xs)
    for elem in np.nditer(xs, flags=["external_loop"]):
        sum += elem
    return sum

def sum_for_numpy_c(xs):
    sum = 0
    xs = np.array(xs)
    for elem in np.nditer(xs, order="C", flags=["external_loop"]):
        sum += elem
    return sum

def sum_for_numpy_f(xs):
    sum = 0
    xs = np.array(xs)
    for elem in np.nditer(xs, order="C", flags=["external_loop"]):
        sum += elem
    return sum

def sum_reduce(xs):
    reduce(lambda x, y: x + y, xs)


print ("### Testing ###\n")

time.sleep(1)

print("sum_for:         "
    + format(timeit.timeit("sum_for(lst)", "from __main__ import sum_for, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_for_range:   "
    + format(timeit.timeit("sum_for_range(lst)", "from __main__ import sum_for_range, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_for_xrange:  "
    + format(timeit.timeit("sum_for_xrange(lst)", "from __main__ import sum_for_xrange, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_for_numpy:   "
    + format(timeit.timeit("sum_for_numpy(lst)", "from __main__ import sum_for_numpy, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_for_numpy_c: "
    + format(timeit.timeit("sum_for_numpy_c(lst)", "from __main__ import sum_for_numpy_c, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_for_numpy_f: "
    + format(timeit.timeit("sum_for_numpy_f(lst)", "from __main__ import sum_for_numpy_f, lst", number=loops), "8.5f") + "s")

time.sleep(1)

print("sum_reduce:      "
    + format(timeit.timeit("sum_reduce(lst)", "from __main__ import sum_reduce, lst", number=loops), "8.5f") + "s")