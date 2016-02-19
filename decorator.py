from functools import wraps


def outer(func):
    @wraps(func)
    def inner():
        ret = func()
        return ret + 1
    return inner


@outer
def foo():
    return 1

print(foo())
print(foo.__name__)


def manipulate(func):
    @wraps(func)
    def inner(a, b):
        a, b = int(a) + 5, int(b)
        return func(a, b)
    return inner

@manipulate
def add(a, b):
    return a + b

print(add(1, 2))
print(add(1.0, 2))
print(add(1, 2.0))
print(add(1.0, 2.0))
