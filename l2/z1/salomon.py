import math


class SalomonFunc(object):

    def __call__(self, vector):
        partial_sum = sum(x_i ** 2 for x_i in vector)
        return 1 - math.cos(2 * math.pi * math.sqrt(partial_sum)) + 0.1 * math.sqrt(partial_sum)
