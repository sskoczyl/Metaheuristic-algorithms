import numpy as np
import time
import random


class Compression(object):

    def __init__(self, base_matrix):
        self.Matrix = base_matrix
        self.BestMatrix = None
        self.best_distance = None

    def get_best_solution(self):
        return self.BestMatrix

    def get_best_distance(self):
        return self.best_distance

    def find_minima(self, max_time, k):
        self.BestMatrix = self.Matrix.get_random_solution(k)
        self.best_distance = self.Matrix.distance_beetween_matrices(self.BestMatrix)
        current_sol = self.BestMatrix
        temp = 10
        epoch = 5
        t_end = time.time() + max_time

        while time.time() < t_end:
            for i in range(epoch):
                temp_sol = self.Matrix.get_neighbour(current_sol, k)
                temp_dist = self.Matrix.distance_beetween_matrices(temp_sol)
                current_dist = self.Matrix.distance_beetween_matrices(current_sol)

                if temp_dist < self.best_distance:
                    self.BestMatrix = temp_sol
                    self.best_distance = temp_dist

                delta = temp_dist - current_dist

                if delta < 0:
                    current_sol = temp_sol
                else:
                    x = random.random()
                    if x < np.exp((-delta) / temp):
                        current_sol = temp_sol

            temp *= 0.9
