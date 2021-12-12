#!/usr/bin/python
# coding=utf-8
import statistics


input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def read_line():
    return input_file.readline()[:-1]


def read_comma_separated_int_line():
    return [int(x) for x in read_line().split(',')]


def solve(positions):
    median = statistics.median(positions)
    fuel = 0
    for x in positions:
        fuel += abs(median - x)

    return int(fuel)


positions = read_comma_separated_int_line()
print_list(positions, 'Positions')
fuel = solve(positions)
print(f'Used fuel: {fuel}')
