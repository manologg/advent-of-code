#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_title(title):
    print('{}:'.format(title) if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print('{}: {}'.format(key, value))


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print('ignoring line \'{}\''.format(line))


def parse(line):
    groupdict = re.match(r'^(?P<key>\w+): (?P<value>\w+)$', line).groupdict()
    return int(groupdict['key']), int(groupdict['value'])


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def read_lines_while_not_empty():
    line = read_line()
    x = []
    while line:
        x.append(line)
        line = read_line()
    return x


def solve(lines):
    # solve the problem
    return True


def test(test_cases):
    for line, expected in test_cases:
        result = solve(line.replace(' ', ''))
        if result == expected:
            print('{} --> OK'.format(line))
        else:
            raise AssertionError('Expected: {}. Found: {}'.format(expected, result))
    print('All tests passed!')


test([
    ...
])

lines = read_lines()
solve(lines)
print_list(lines, 'Input')
