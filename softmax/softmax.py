from distributions.gaussian_distribution import Gaussian
from matplotlib import pyplot as plt
import numpy as np


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


norm_distri = Gaussian.get_normal_distribution(shape=(0, 800), mu=400.0, sigma=20.0)
norm_distri_noise = norm_distri * 2 + np.random.rand(800) * 0.04 - 0.02
norm_distri_noise[:200] -= 0.01
norm_distri_noise[:100] -= 0.01
norm_distri_noise[600:] -= 0.01
norm_distri_noise[700:] -= 0.01
norm_distri_noise_softmax = softmax(norm_distri_noise)


plt.plot(norm_distri, linestyle="solid", color="blue", label="teacher")
plt.plot(norm_distri_noise, marker="x", linestyle="solid", color="red", label="out linear")
plt.plot(norm_distri_noise_softmax, marker="x", linestyle="solid", color="green", label="out softmax")
plt.legend()

plt.show()
