#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_list(l, title=''):
    print(f'{title}: {",".join([str(x) for x in l])}')


def read_line():
    return input_file.readline()[:-1]


def read_comma_separated_int_line():
    return [int(x) for x in read_line().split(',')]


def cycle(population):
    new_population = dict()
    for i in range(8):
        new_population[i] = population[i + 1]

    new_population[6] += population[0]
    new_population[8] = population[0]

    return new_population


def solve(population, days):
    print_list(population.items(), f'Initial state ')
    for i in range(1, days + 1):
        population = cycle(population)
        # print_list(population.items(), f'After {str(i).rjust(3, " ")} days')
        print(f'After {str(i).rjust(3, " ")} days: {sum(population.values())}')

    return population


population = read_comma_separated_int_line()
population = {x: population.count(x) for x in range(9)}
population = solve(population, days=256)
print(f'Population size: {sum(population.values())}')
