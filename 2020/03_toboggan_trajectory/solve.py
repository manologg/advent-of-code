#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def print_map(slope):
    for line in slope:
        print(line)
    print()


line = readline()
slope = []
while line:
    slope.append(line)
    line = readline()

print_map(slope)

max_i = len(slope) - 1
max_j = len(slope[0])


def solve(start_i, start_j):
    i = start_i
    j = start_j
    trees = 0

    while i <= max_i:

        print('I\'m at ({}, {}) --> {}'.format(i, j, slope[i][j]))

        if slope[i][j] == '#':
            trees += 1

        i = i + start_i
        j = (j + start_j) % max_j

    print("Encountered trees ({}, {}): {}".format(start_i, start_j, trees))
    return trees


mutiplied_trees = solve(1, 1) * solve(1, 3) * solve(1, 5) * solve(1, 7) * solve(2, 1)
print("Encountered multiplied trees: {}".format(mutiplied_trees))
