#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def parse(line):
    return [x for x in line]


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def solve(lines):
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(lines[0])):
        column = [line[i] for line in lines]
        zeroes = column.count('0')
        ones = column.count('1')
        if ones > zeroes:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2), int(epsilon_rate, 2)


array = read_and_parse_lines()
gamma_rate, epsilon_rate = solve(array)
print(f'Multiplication of gamma rate by epsilon rate: {gamma_rate} * {epsilon_rate} = {gamma_rate*epsilon_rate}')


