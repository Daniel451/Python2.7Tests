import numpy as np

class Gaussian:

    @staticmethod
    def get_normal_distribution(shape=(0, 10), mu=0.0, sigma=1.0):
        # discrete gaussian vector
        data_buffer = np.arange(shape[0], shape[1])

        data_buffer = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (data_buffer - mu) ** 2 / (2 * sigma ** 2))

        return data_buffer
