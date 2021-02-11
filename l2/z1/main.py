from salomon import SalomonFunc
from annealing import SimulatedAnnealing


def main():
    in_data = input()
    vector = list(map(float, in_data.split()))
    time = vector[0]
    vector.pop(0)

    Searcher = SimulatedAnnealing(SalomonFunc())
    Searcher.find_minima(time, vector)

    sol_vect = Searcher.get_best_solution()

    for x_i in sol_vect:
        print(x_i, end=' ')

    print(Searcher.get_best_value())


if __name__ == '__main__':
    main()
