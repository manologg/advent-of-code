#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print(f'{key}: {value}')


def print_simple_list(l, title):
    print(f'{title}: {", ".join([str(x) for x in l])}')


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print(f'ignoring line \'{line}\'')


def get_digit_strs(numbers):
    return [sorted(x) for x in numbers.split(' ')]


def parse(line):
    groupdict = re.match(r'^(?P<input>[a-g ]+) \| (?P<output>[a-g ]+)$', line).groupdict()
    return get_digit_strs(groupdict['output'])


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def solve(lines):
    amount = 0
    for line in lines:
        amount += sum([1 for x in line if len(x) in [2, 3, 4, 7]])
    return amount


def print_solution(digits, output):
    pass


lines = read_and_parse_lines()
amount = solve(lines)
print(f'1, 4, 7 and 8 appear {amount} times')
