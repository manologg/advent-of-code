#!/usr/bin/python
# coding=utf-8
import itertools
import re

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)
    print()


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print(f'{key}: {value}')
    print()


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()


def parse(line):
    groupdict = re.match(r'^(?P<key>\w+) -> (?P<value>\w+)$', line).groupdict()
    return groupdict['key'], groupdict['value']


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def read_lines():
    template = read_line()
    ignore_line()
    rules = read_and_parse_lines()
    return template, dict(rules)


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def step(polymer, rules):
    new_polymer = []

    for current, next in pairwise(polymer):
        new_polymer.append(current)
        new_polymer.append(rules[current + next])

    # don't forget the last one
    new_polymer.append(polymer[-1])

    return new_polymer


def solve(polymer, rules, steps):
    for i in range(steps):
        polymer = step(polymer, rules)
        print(f'After step {i+1:>2}: {"".join(polymer)}')
    return polymer


template, rules = read_lines()
# print_list(rules, 'Rules')
print(f'Template:      {template}')
polymer = solve(template, rules, steps=10)
elements = [polymer.count('B'), polymer.count('C'), polymer.count('H'), polymer.count('N')]
print(f'Quantity of the most common element - quantity of the least common element: {max(elements)} - {min(elements)} = {max(elements) - min(elements)}')

