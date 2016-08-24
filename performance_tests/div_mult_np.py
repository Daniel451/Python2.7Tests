import numpy as np
import timeit

# uint8 array
arr1 = np.random.randint(0, high=256, size=(100, 100), dtype=np.uint8) 

# float32 array
arr2 = np.random.rand(100, 100).astype(np.float32)
arr2 *= 255.0


def arrmult(a):
    """
    mult, read-write iterator
    """
    b = a.copy()
    for item in np.nditer(b, op_flags=["readwrite"]):
        item[...] = (item + 5) * 0.5

def arrmult2(a):
    """
    mult, index iterator
    """
    b = a.copy()
    for i, j in np.ndindex(b.shape):
        b[i, j] = (b[i, j] + 5) * 0.5

def arrmult3(a):
    """
    mult, vectorized
    """
    b = a.copy()
    b = (b + 5) * 0.5

def arrdiv(a):
    """
    div, read-write iterator
    """
    b = a.copy()
    for item in np.nditer(b, op_flags=["readwrite"]):
        item[...] = (item + 5) / 2

def arrdiv2(a):
    """
    div, index iterator
    """
    b = a.copy()
    for i, j in np.ndindex(b.shape):
        b[i, j] = (b[i, j] + 5) / 2

def arrdiv3(a):
    """
    div, vectorized
    """
    b = a.copy()
    b = (b + 5) / 0.5




def print_time(name, t):
    print("{: <10}: {: >6.4f}s".format(name, t))

timeit_iterations = 100

print("uint8 arrays")
print_time("arrmult", timeit.timeit("arrmult(arr1)", "from __main__ import arrmult, arr1", number=timeit_iterations))
print_time("arrmult2", timeit.timeit("arrmult2(arr1)", "from __main__ import arrmult2, arr1", number=timeit_iterations))
print_time("arrmult3", timeit.timeit("arrmult3(arr1)", "from __main__ import arrmult3, arr1", number=timeit_iterations))
print_time("arrdiv", timeit.timeit("arrdiv(arr1)", "from __main__ import arrdiv, arr1", number=timeit_iterations))
print_time("arrdiv2", timeit.timeit("arrdiv2(arr1)", "from __main__ import arrdiv2, arr1", number=timeit_iterations))
print_time("arrdiv3", timeit.timeit("arrdiv3(arr1)", "from __main__ import arrdiv3, arr1", number=timeit_iterations))

print("\nfloat32 arrays")
print_time("arrmult", timeit.timeit("arrmult(arr2)", "from __main__ import arrmult, arr2", number=timeit_iterations))
print_time("arrmult2", timeit.timeit("arrmult2(arr2)", "from __main__ import arrmult2, arr2", number=timeit_iterations))
print_time("arrmult3", timeit.timeit("arrmult3(arr2)", "from __main__ import arrmult3, arr2", number=timeit_iterations))
print_time("arrdiv", timeit.timeit("arrdiv(arr2)", "from __main__ import arrdiv, arr2", number=timeit_iterations))
print_time("arrdiv2", timeit.timeit("arrdiv2(arr2)", "from __main__ import arrdiv2, arr2", number=timeit_iterations))
print_time("arrdiv3", timeit.timeit("arrdiv3(arr2)", "from __main__ import arrdiv3, arr2", number=timeit_iterations))


