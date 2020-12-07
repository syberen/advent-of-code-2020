from functions import find_pair, find_triplet


with open('input.txt', 'r') as input:
    all_values = [int(line.rstrip()) for line in input.readlines()]

    a, b = find_pair(all_values, 2020)

    c, d, e = find_triplet(all_values, 2020)

    print(a * b)
    print(c * d * e)
