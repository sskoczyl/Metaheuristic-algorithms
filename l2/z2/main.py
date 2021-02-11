import sys
from matrix import Matrix
from compression import Compression


def main():
    in_data = input()
    in_data = list(map(int, in_data.split()))
    matrix = []

    for i in range(in_data[1]):
        matrix.append(list(map(int, input().split())))

    mx1 = Matrix(matrix)
    Search = Compression(mx1)
    Search.find_minima(in_data[0], in_data[3])

    for i in Search.get_best_solution():
        for j in i:
            print(j, file=sys.stderr, end=' ')

        print(file=sys.stderr)

    print(Search.get_best_distance())


if __name__ == '__main__':
    main()
