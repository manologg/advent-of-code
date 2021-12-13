#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def print_map(m, title=''):
    print_title(title)
    for line in m:
        print(' '.join([str(x) for x in line]))
    print()


def read_line():
    return input_file.readline()[:-1]


def parse(line):
    groupdict = re.match(r'^fold along (?P<axis>\w+)=(?P<number>\w+)$', line).groupdict()
    return groupdict['axis'], int(groupdict['number'])


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def read_lines_while_not_empty():
    line = read_line()
    lines = set()
    while line:
        x, y = line.split(',')
        lines.add((int(x), int(y)))
        line = read_line()
    return lines


def read_lines():
    return read_lines_while_not_empty(), read_and_parse_lines()


def fold(dots, axis, number):

    if axis == 'y':
        result = {(x, y) for x, y in dots if y < number}
        for x, y in dots:
            if y > number:
                result.add((x, number - (y - number)))
        return result

    elif axis == 'x':
        result = {(x, y) for x, y in dots if x < number}
        for x, y in dots:
            if x > number:
                result.add((number - (x - number), y))
        return result

    else:
        raise NotImplementedError()


def solve(dots, commands):

    for i, command in enumerate(commands):
        dots = fold(dots, *command)
        print_list(sorted(dots), f'Dots after {i} fold(s)')
        print()

    return dots


def print_dots(dots):
    max_x = max([x for x, y in dots]) + 1
    max_y = max([y for x, y in dots]) + 1
    m = [[' '] * max_x for _ in range(max_y)]
    for x, y in dots:
        m[y][x] = '#'

    print_map(m, 'Final dots')


dots, commands = read_lines()
print_list(sorted(dots), 'Dots')
print()
print_list(commands, 'Commands')
print()
dots = solve(dots, commands)
print(f'{len(dots)} dots are visible after completing {len(commands)} fold(s)')
print_dots(dots)
