import numpy as np

def test(a,b,c):
    print(a+b+c)

vtest = np.vectorize(test)

arr = np.arange(9).reshape(3,3)

vtest(arr,arr,arr)
