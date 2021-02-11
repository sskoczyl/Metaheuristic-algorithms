import numpy as np


class XSYang:

    def __init__(self, e):
        self.epsilons = e

    def __call__(self, vector):
        out = 0

        for i in range(len(vector)):
            out += self.epsilons[i] * np.float_power(abs(vector[i]), i+1)

        return out
