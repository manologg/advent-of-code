#!/usr/bin/python
# coding=utf-8
import cProfile
import io
import re
from pstats import SortKey, Stats

input_file = open('input.txt')


def run_with_profiling(func, *args, **kwargs):
    profile = cProfile.Profile()
    profile.enable()

    # run the code
    result = func(*args, **kwargs)

    profile.disable()
    stream = io.StringIO()
    sort_by = SortKey.CUMULATIVE
    stats = Stats(profile, stream=stream).sort_stats(sort_by)
    stats.print_stats()
    print(stream.getvalue())

    return result


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


def print_grid(grid, title=''):
    print_title(title)
    for line in grid:
        print(' '.join([str(x) for x in line]))
    print()


def print_simple_list(l, title):
    print(f'{title}: {",".join([str(x) for x in l])}')


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print(f'ignoring line \'{line}\'')


def parse(line):
    groupdict = re.match(r'^(?P<key>\w+): (?P<value>\w+)$', line).groupdict()
    return int(groupdict['key']), int(groupdict['value'])


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def read_comma_separated_int_line():
    return [int(x) for x in read_line().split(',')]


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def read_lines_while_not_empty():
    line = read_line()
    x = []
    while line:
        x.append(line)
        line = read_line()
    return x


def move_dial(dial, line):
    direction = line[0]
    amount = int(line[1:])
    if direction == 'R':
        dial = (dial + amount) % 100
    elif direction == 'L':
        dial = (dial - amount) % 100
    return dial


def solve(lines):
    dial = 50
    pointing_0 = 0
    for line in lines:
        dial = move_dial(dial, line)
        if dial == 0:
            pointing_0 += 1
    return pointing_0


def test(test_cases):
    for line, expected in test_cases:
        result = solve(line)
        if result == expected:
            print(f'{line} --> OK')
        else:
            raise AssertionError(f'Expected: {expected}. Found: {result}')
    print('All tests passed!')
    print()


test([
    (["L50", "R50"], 1)
])

# lines = read_lines_while_not_empty()
# print_list(lines, 'Input')
# print(f'Amount of zeros: {solve(lines)}')
