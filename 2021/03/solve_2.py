#!/usr/bin/python
# coding=utf-8
import copy

import ipdb

input_file = open('input.txt')


def parse(line):
    return [x for x in line]


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def get_rating(lines, criteria):
    remaining_lines = copy.deepcopy(lines)
    for i in range(len(lines[0])):
        column = [line[i] for line in remaining_lines]
        zeroes = column.count('0')
        ones = column.count('1')
        if criteria(zeroes, ones):
            remaining_lines = [line for line in remaining_lines if line[i] == '1']
        else:
            remaining_lines = [line for line in remaining_lines if line[i] == '0']

        if len(remaining_lines) == 1:
            return int(''.join(remaining_lines[0]), 2)


def solve(lines):
    o = get_rating(lines, lambda zeroes, ones: ones >= zeroes)
    co2 = get_rating(lines, lambda zeroes, ones: ones < zeroes)
    return o, co2


array = read_and_parse_lines()
oxygen_lines, co2_lines = solve(array)
print(f'Multiplication of gamma rate by epsilon rate: {oxygen_lines} * {co2_lines} = {oxygen_lines*co2_lines}')
