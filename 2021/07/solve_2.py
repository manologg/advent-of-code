#!/usr/bin/python
# coding=utf-8
import statistics
import sys

input_file = open('input.txt')


def print_list(l, title=''):
    print(f'{title}: {",".join([str(x) for x in l])}')


def read_line():
    return input_file.readline()[:-1]


def read_comma_separated_int_line():
    return [int(x) for x in read_line().split(',')]


def triangular_number_count(x):
    return (x * (x+1)) // 2


def solve_for_goal(goal, positions):
    fuel = 0
    for x in positions:
        fuel += triangular_number_count(abs(goal - x))

    return int(fuel)


def solve(positions):

    fuel = sys.maxsize
    goal = 0

    for x in range(max(positions) + 1):
        new_fuel = solve_for_goal(x, positions)
        # print(f'Used fuel: {new_fuel} (moving to position {x})')
        if new_fuel < fuel:
            fuel = new_fuel
            goal = x

    return fuel, goal



positions = read_comma_separated_int_line()
print_list(positions, 'Positions')
fuel, goal = solve(positions)
print(f'Used fuel: {fuel} (moving to position {goal})')
