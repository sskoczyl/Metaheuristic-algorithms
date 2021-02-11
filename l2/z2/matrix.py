import random


class Matrix(object):

    def __init__(self, arr):
        self.matrix = arr
        self.height = len(arr)
        self.length = len(arr[0])

    def distance_beetween_matrices(self, other_matrix):
        return sum(sum((self.matrix[i][j] - other_matrix[i][j]) ** 2 for j in range(self.length))
                   for i in range(self.height)) / (self.height * self.length)

    def get_random_solution(self, k):
        k_h = self.height // k
        k_l = self.length // k
        sectors = []
        solution = []

        for i in range(k_h):
            sectors.append([])

        for i in range(k_h):
            for j in range(k_l):
                sectors[i].append(random.choice([0, 32, 64, 128, 160, 192, 223, 255]))

        for i in range(self.height):
            solution.append([])

        y = 0
        for i in range(self.height):
            x = 0

            if i > 0 and i % k == 0 and y + 1 < len(sectors):
                y += 1

            for j in range(self.length):
                if j > 0 and j % k == 0 and x + 1 < len(sectors[0]):
                    x += 1
                solution[i].append(sectors[y][x])

        return solution

    def get_neighbour(self, solution, k):
        color = [0, 32, 64, 128, 160, 192, 223, 255]
        new_vl = [color[(color.index(solution[0][0]) + random.randint(-1, 1)) % 8]]
        new_solution = []

        idx = 0
        diff = False

        for row_idx in range(self.height):
            row = []

            new_vl.append(color[(color.index(solution[row_idx][0]) + random.randint(-1, 1)) % 8]) \
                if len(new_vl) == 0 else None

            for column_idx in range(self.length):
                row.append(new_vl[idx])

                if (column_idx + 1) % k == 0 and self.length - column_idx - 1 >= k:
                    idx += 1
                    new_vl.append(color[(color.index(solution[row_idx][column_idx + 1]) + random.randint(-1, 1)) % 8]) \
                        if column_idx + 1 < self.length and diff is False else None

            idx = 0
            new_solution.append(row)

            if (row_idx + 1) % k == 0 and self.length - row_idx - 1 >= k:
                diff, new_vl = False, []
            else:
                diff = True

        return new_solution
