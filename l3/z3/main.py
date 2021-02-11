import sys
from agent import Agent
from maze import Genetic
import numpy as np


def main():
    in_data = input()
    in_data = list(map(int, in_data.split()))
    matrix = []
    time = in_data[0]

    for i in range(in_data[1]):
        matrix.append(list(map(int, input().replace('\r', ''))))

    start_sol = []

    for i in range(in_data[3]):
        start_sol.append(input().replace('\r', ''))
    a = Agent(np.array(matrix))
    Searcher = Genetic(Agent(np.array(matrix)), in_data[4])
    Searcher.find_minima(start_sol, time)

    print(Searcher.get_best_value())
    print(Searcher.get_best_solution(), file=sys.stderr)


if __name__ == '__main__':
    main()
