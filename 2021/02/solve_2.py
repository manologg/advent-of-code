#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def print_title(title):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def parse(line):
    direction, amount = line.split(' ')
    return direction, int(amount)


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def solve(lines):
    horizontal_position = 0
    depth = 0
    aim = 0

    for direction, amount in lines:
        if direction == 'down':
            aim += amount
        if direction == 'up':
            aim -= amount
        if direction == 'forward':
            horizontal_position += amount
            depth += aim * amount

    return horizontal_position, depth


lines = read_and_parse_lines()
horizontal_position, depth = solve(lines)
print_list(lines, 'Input')
print(f'Multiplication of horizontal position by depth: {horizontal_position} * {depth} = {horizontal_position*depth}')
