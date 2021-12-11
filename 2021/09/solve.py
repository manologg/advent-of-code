#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def print_simple_list(l, title):
    print(f'{title}: {",".join([str(x) for x in l])}')


def read_lines():
    return [[int(x) for x in line[:-1]] for line in input_file.readlines()]


def solve(m):
    max_i = len(m) - 1
    max_j = len(m[0]) - 1
    sum = 0
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            point = m[i][j]
            if (i == 0 or point < m[i - 1][j]) \
                    and (i == max_i or point < m[i + 1][j]) \
                    and (j == 0 or point < m[i][j - 1]) \
                    and (j == max_j or point < m[i][j + 1]):
                sum += point + 1
    return sum


lines = read_lines()
print_list(lines, 'Input')
sum = solve(lines)
print(f'Sum of the risk levels of all low points: {sum}')
