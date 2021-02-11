import sys
from agent import Agent
from maze import SimulatedAnnealing
import numpy as np


def main():
    in_data = input()
    in_data = list(map(int, in_data.split()))
    matrix = []

    for i in range(in_data[1]):
        matrix.append(list(map(int, list(input().replace('\r', '')))))

    Searcher = SimulatedAnnealing(Agent(np.array(matrix)))
    Searcher.find_minima(in_data[0])

    print(Searcher.get_best_value())

    for i in Searcher.get_best_solution():
        print(i, file=sys.stderr, end='')

    print(file=sys.stderr)


if __name__ == '__main__':
    main()
