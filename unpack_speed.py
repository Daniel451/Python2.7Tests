import timeit



def without_unpack():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10

    cont = [a, b, c, d, e, f, g, h, i, j]

    return cont


def with_unpack():
    a, b, c, d, e, f, g, h, i, j = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    cont = [a, b, c, d, e, f, g, h, i, j]

    return cont

print(timeit.timeit("without_unpack", "from __main__ import without_unpack", number=100000000))

print(timeit.timeit("with_unpack", "from __main__ import with_unpack", number=100000000))
