import multiprocessing
import numpy as np
import timeit
import time


def sum_worker(q, xs):
    q.put(reduce(lambda x, y: x + y, xs))


def sum_it_up(xs, num_threads = 4):
    queue = multiprocessing.Queue()
    worker = []

    part_low = 0
    part_high = len(xs)/num_threads

    for i in range(0, num_threads):
        worker.append(multiprocessing.Process(target=sum_worker, args=(queue, xs[part_low:part_high])))
        worker[i].start()
        part_low += len(xs)/num_threads
        part_high += len(xs)/num_threads

    for i in range(0, num_threads):
        worker[i].join()

    result_list = []

    while not queue.empty():
        result_list.append(queue.get())

    sum_worker(queue, result_list)

    return queue.get()


lst = list(np.random.randint(1, 100, 10000000))

print("Starting reduce - single core")
time_single = timeit.timeit("reduce(lambda x, y: x + y, lst)", "from __main__ import lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 2 cores")
time_parallel_2cores = timeit.timeit("sum_it_up(lst, 2)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 3 cores")
time_parallel_3cores = timeit.timeit("sum_it_up(lst, 3)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 4 cores")
time_parallel_4cores = timeit.timeit("sum_it_up(lst, 4)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 5 cores")
time_parallel_5cores = timeit.timeit("sum_it_up(lst, 5)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 6 cores")
time_parallel_6cores = timeit.timeit("sum_it_up(lst, 6)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 7 cores")
time_parallel_7cores = timeit.timeit("sum_it_up(lst, 7)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("Starting reduce - 8 cores")
time_parallel_8cores = timeit.timeit("sum_it_up(lst, 8)", "from __main__ import sum_it_up, lst", number=10)
print("done!\n")

time.sleep(1)

print("\nResults:\n")

print("1 core : {0:8.5f}s").format(time_single)
print("2 cores: {0:8.5f}s").format(time_parallel_2cores)
print("3 cores: {0:8.5f}s").format(time_parallel_3cores)
print("4 cores: {0:8.5f}s").format(time_parallel_4cores)
print("5 cores: {0:8.5f}s").format(time_parallel_5cores)
print("6 cores: {0:8.5f}s").format(time_parallel_6cores)
print("7 cores: {0:8.5f}s").format(time_parallel_7cores)
print("8 cores: {0:8.5f}s").format(time_parallel_8cores)
