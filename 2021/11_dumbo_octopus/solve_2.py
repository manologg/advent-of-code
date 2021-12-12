#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_map(m, title=''):
    print_title(title)
    for line in m:
        print(' '.join([str(x) for x in line]))


def read_lines():
    return [[int(x) for x in line[:-1]] for line in input_file.readlines()]


def level_up_neighbours(m, i, j, max_i, max_j, flashed_octopuses):
    for ii in [i - 1, i, i + 1]:
        for jj in [j - 1, j, j + 1]:

            if 0 <= ii <= max_i \
                    and 0 <= jj <= max_j \
                    and (ii, jj) not in flashed_octopuses:
                m[ii][jj] += 1


def step(m, max_i, max_j):
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            m[i][j] += 1

    flashes = 0
    flashed_octopuses = []

    while True:

        new_flashes = 0

        # go through all the octopuses
        for i in range(max_i + 1):
            for j in range(max_j + 1):

                # it flashed
                if m[i][j] > 9:
                    m[i][j] = 0
                    flashed_octopuses.append((i, j))
                    new_flashes += 1
                    level_up_neighbours(m, i, j, max_i, max_j, flashed_octopuses)

        if not new_flashes:
            break

        flashes += new_flashes

    return flashes


def solve(m):
    max_i = len(m) - 1
    max_j = len(m[0]) - 1
    print_map(m, 'Step 0')
    i = 0
    while True:
        i += 1
        flashes = step(m, max_i, max_j)
        print_map(m, f'Step {i} ({flashes} flashes)')
        print()
        if flashes == (max_i + 1) * (max_j + 1):
            return i


lines = read_lines()
first_step = solve(lines)
print(f'First step during which all octopuses flash: {first_step}')
