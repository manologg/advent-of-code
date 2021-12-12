#!/usr/bin/python
# coding=utf-8
import math

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def read_lines():
    return [[int(x) for x in line[:-1]] for line in input_file.readlines()]


def count_basin_points(i, j, m, max_i, max_j, visited):
    if m[i][j] == 9 or (i, j) in visited:
        return 0

    visited.append((i, j))

    top = 0 if i == 0 else count_basin_points(i - 1, j, m, max_i, max_j, visited)
    bottom = 0 if i == max_i else count_basin_points(i + 1, j, m, max_i, max_j, visited)
    left = 0 if j == 0 else count_basin_points(i, j - 1, m, max_i, max_j, visited)
    right = 0 if j == max_j else count_basin_points(i, j + 1, m, max_i, max_j, visited)

    return 1 + top + bottom + left + right


def solve(m):
    max_i = len(m) - 1
    max_j = len(m[0]) - 1
    basin_points = []
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            point = m[i][j]
            if (i == 0 or point < m[i - 1][j]) \
                    and (i == max_i or point < m[i + 1][j]) \
                    and (j == 0 or point < m[i][j - 1]) \
                    and (j == max_j or point < m[i][j + 1]):
                basin_points.append(count_basin_points(i, j, m, max_i, max_j, []))
    return math.prod(sorted(basin_points, reverse=True)[:3])


lines = read_lines()
print_list(lines, 'Input')
sum = solve(lines)
print(f'Sum of the risk levels of all low points: {sum}')
