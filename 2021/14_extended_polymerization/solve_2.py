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
    print()


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print(f'{key}: {value}')
    print()


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    read_line()


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


def prepare_polymer(template):
    polymer = dict()

    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        amount = polymer.get(pair, 0)
        polymer[pair] = amount + 1

    return polymer


def step(polymer, rules):
    new_polymer = dict()
    for pair, amount in polymer.items():
        new_char = rules[pair]
        for new_pair in [pair[0] + new_char, new_char + pair[1]]:
            new_amount = new_polymer.get(new_pair, 0)
            new_polymer[new_pair] = new_amount + amount

    return new_polymer


def solve(template, rules, steps):
    polymer = prepare_polymer(template)
    for i in range(steps):
        polymer = step(polymer, rules)
        print(f'After step {i+1:>2} the polymer has {len(polymer.keys())} pairs')
        print(f'Polymer: {polymer}')

    return polymer


def unique_chars(polymer):
    return set([c for chars in polymer.keys() for c in chars])


def print_solution(polymer):
    count = {c: 0 for c in unique_chars(polymer)}

    # count all (double)
    for pair, amount in polymer.items():
        first = pair[0]
        second = pair[1]
        count[first] += amount
        count[second] += amount

    # divide by 2
    count = {c: amount // 2 if amount % 2 == 0 else (amount - 1) // 2 + 1
             for c, amount in count.items()}

    print(f'Quantity of the most common element - quantity of the least common element: '
          f'{max(count.values())} - {min(count.values())} = {max(count.values()) - min(count.values())}')


template, rules = read_lines()
# print_list(rules, 'Rules')
print(f'Template:      {template}')
polymer = solve(template, rules, steps=40)
print_solution(polymer)

