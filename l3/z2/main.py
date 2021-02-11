from genetic import Genetic
import sys


def main():
    in_data = input()
    vector = list(map(int, in_data.split()))
    time = vector[0]
    vector.pop(0)

    multiset = []
    values = {}

    for i in range(vector[0]):
        in_data = input()
        x = list(map(str, in_data.split()))
        multiset.append(x[0])
        values[x[0]] = int(x[1])

    start_sol = []

    for i in range(vector[1]):
        in_data = input().replace("\r", "")
        start_sol.append(in_data)

    Searcher = Genetic('dict.txt', values, multiset, 100)
    Searcher.find_maxima(start_sol, time)

    print(Searcher.best_value())
    print(Searcher.best_argument(), file=sys.stderr)


if __name__ == '__main__':
    main()
