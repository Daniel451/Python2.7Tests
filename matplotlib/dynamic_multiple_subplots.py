from matplotlib import pyplot as plt
import numpy as np


a = np.random.rand(100)
b = np.random.rand(100)
c = np.random.rand(100)


def plotA(ax, data):
    pass


def plotB(ax, data):
    pass


def dispatcher(data, list_of_plot_types):
    function_map = {'A': plotA, 'B': plotB}
    fig, list_of_axes = plt.subplots(1, len(list_of_plot_types))

    for ax, plot_type in zip(list_of_axes, list_of_plot_types):
        function_map[plot_type](ax, data)
