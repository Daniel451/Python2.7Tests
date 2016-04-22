from functools import wraps
from itertools import izip



def accepts(*types):
    """
    top-level decoration, consumes parameters
    """

    def decorator(func):
        """
        actual decorator function, consumes the input function
        """

        @wraps(func)
        def check_accepts(*args):
            """
            actual wrapper which does some magic type-checking
            """
            # check if length of args matches length of specified types
            assert len(args) == len(types), "{} arguments were passed to func '{}' but only {} " \
                                            "types were passed to decorator '@accepts'" \
                                            .format(len(args), func.__name__, len(types))

            # check types of arguments
            for i, arg, typecheck in izip(range(1, len(args)+1), args, types):
                assert isinstance(arg, typecheck), "type checking: argument #{} was expected to be {} but is {}"\
                                                    .format(i, typecheck, type(arg))

        return check_accepts

    return decorator


@accepts(int, float, str)
def test(a, b, c):
    print a, b, c


test(2, 2.0, "hallo")
# test(2.0, 2.0, "hallo")
# test(2, 2, "hallo")
# test(2.0, 2, "hallo")
#test("a", "a", 2)
#test(2, 2.0, 2)

print(test.__name__)
a = test
print(a.__name__)
