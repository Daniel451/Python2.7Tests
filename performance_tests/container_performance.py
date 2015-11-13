from collections import OrderedDict
import numpy as np
import time
import timeit

low = 0
high = 100000
size = 1000000
timeit_iterations = 100
get_item_nr = int(size/2)
search_for = np.random.randint(low, high)

spacer = 10

t_lst = list(np.random.randint(low, high, size))
t_tuple = tuple(t_lst)
t_dict = {i: t_lst[i] for i in range(0, len(t_lst))}
t_odict = OrderedDict({i: t_lst[i] for i in range(0, len(t_lst))})


############################
### search in collection ###
############################

def search_in_dict(d, search):
    for key, val in d.iteritems():
        if val == search:
            return key


print ("\nSearching in collections for {0}:\n").format(search_for)

time.sleep(0.5)

print("list: ".ljust(spacer, " ")
      + "{0:7.4f}"
      .format(
    timeit.timeit("t_lst.index(search_for)", "from __main__ import search_for, t_lst", number=timeit_iterations)

) + "s")

time.sleep(0.5)

print("tuple: ".ljust(spacer, " ")
      + "{0:7.4f}"
      .format(
    timeit.timeit("t_tuple.index(search_for)", "from __main__ import search_for, t_tuple", number=timeit_iterations)
) + "s")

time.sleep(0.5)

print("dict: ".ljust(spacer, " ")
      + "{0:7.4f}"
      .format(
    timeit.timeit("search_in_dict(t_dict, search_for)", "from __main__ import search_for, t_dict, search_in_dict", number=timeit_iterations)
) + "s")

time.sleep(0.5)

print("odict: ".ljust(spacer, " ")
      + "{0:7.4f}"
      .format(
    timeit.timeit("search_in_dict(t_odict, search_for)", "from __main__ import search_for, t_odict, search_in_dict", number=timeit_iterations)
) + "s")


################
### get item ###
################

print ("\nGet item for key {0} in collections:\n").format(get_item_nr)

time.sleep(0.5)

print("list: ".ljust(spacer, " ")
      + "{0:7.30f}"
      .format(
    timeit.timeit("t_lst[get_item_nr]", "from __main__ import get_item_nr, t_lst", number=timeit_iterations)

) + "s")

time.sleep(0.5)

print("tuple: ".ljust(spacer, " ")
      + "{0:7.30f}"
      .format(
    timeit.timeit("t_tuple[get_item_nr]", "from __main__ import get_item_nr, t_tuple", number=timeit_iterations)
) + "s")

time.sleep(0.5)

print("dict: ".ljust(spacer, " ")
      + "{0:7.30f}"
      .format(
    timeit.timeit("t_dict[get_item_nr]", "from __main__ import get_item_nr, t_dict", number=timeit_iterations)
) + "s")

time.sleep(0.5)

print("odict: ".ljust(spacer, " ")
      + "{0:7.30f}"
      .format(
    timeit.timeit("t_odict[get_item_nr]", "from __main__ import get_item_nr, t_odict", number=timeit_iterations)
) + "s")

