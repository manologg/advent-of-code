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
    new_population = []
    for i, x in enumerate(population):
        population[i] -= 1
        if population[i] == -1:
            population[i] = 6
            new_population.append(8)

    population.extend(new_population)


def solve(population, days):
    print_list(population, 'Initial state')
    for i in range(1, days + 1):
        cycle(population)
        # print_list(population, f'After {str(i).rjust(3, " ")} days')
        print(f'After {str(i).rjust(3, " ")} days: {len(population)}')

    return population


population = read_comma_separated_int_line()
population = solve(population, days=256)
print(f'Population size: {len(population)}')
