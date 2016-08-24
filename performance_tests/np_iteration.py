import numpy as np
import timeit

# uint8 array
arr1 = np.random.randint(0, high=256, size=(100, 100), dtype=np.uint8) 

# float32 array
arr2 = np.random.rand(100, 100).astype(np.float32)
arr2 *= 255.0


def nditer(a):
    """
    read-write iterator
    """
    b = a.copy()
    for item in np.nditer(b, op_flags=["readwrite"]):
        item[...] = item + 5

def ndindex(a):
    """
    index iterator
    """
    b = a.copy()
    for x, y in np.ndindex(b.shape):
        b[x, y] += 5

def ndenumerate(a):
    """
    ndenumerate iterator
    """
    b = a.copy()
    for key, val in np.ndenumerate(b):
        b[key] += 5

def vectorize(a):
    """
    vectorized function
    """
    b = a.copy()
    b += 5


def print_time(name, t):
    print("{:.<12}:  {: >6.4f}s".format(name, t))

timeit_iterations = 100

print("uint8 arrays")
print_time("nditer", timeit.timeit("nditer(arr1)", "from __main__ import nditer, arr1", number=timeit_iterations))
print_time("ndindex", timeit.timeit("ndindex(arr1)", "from __main__ import ndindex, arr1", number=timeit_iterations))
print_time("ndenumerate", timeit.timeit("ndenumerate(arr1)", "from __main__ import ndenumerate, arr1", number=timeit_iterations))
print_time("vectorize", timeit.timeit("vectorize(arr1)", "from __main__ import vectorize, arr1", number=timeit_iterations))

print("\nfloat32 arrays")
print_time("nditer", timeit.timeit("nditer(arr2)", "from __main__ import nditer, arr2", number=timeit_iterations))
print_time("ndindex", timeit.timeit("ndindex(arr2)", "from __main__ import ndindex, arr2", number=timeit_iterations))
print_time("ndenumerate", timeit.timeit("ndenumerate(arr2)", "from __main__ import ndenumerate, arr2", number=timeit_iterations))
print_time("vectorize", timeit.timeit("vectorize(arr2)", "from __main__ import vectorize, arr2", number=timeit_iterations))


