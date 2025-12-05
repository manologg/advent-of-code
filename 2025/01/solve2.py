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


def solve(lines):
    dial = 50
    pointing_0 = 0
    for line in lines:

        direction = line[0]
        amount = int(line[1:])

        old_dial = dial

        # move dial
        if direction == 'R':
            new_dial = dial + amount
        else:
            new_dial = dial - amount

        dial = new_dial % 100

        if dial != new_dial:
            diff = abs(new_dial // 100)
            pointing_0 += diff
            # print(f'The dial is rotated {line} to point at {dial}; during this rotation, it points at zero {diff} times.')
        # else:
        #     print(f'The dial is rotated {line} to point at {dial}.')

        if dial == 0 and direction == 'L':
            pointing_0 += 1
            # print(f'Count one more because we ended at zero')
        if old_dial == 0 and direction == 'L':
            pointing_0 -= 1
            # print(f'Count one less because we started at zero and went left')

        # print()

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
    (['L150'], 2),
    (['L50'], 1),
    (['L50', 'R1', 'L2'], 2),
    (['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'], 6),
    (['L68', 'L30', 'R48', 'L5', 'R60', 'L155', 'L1', 'L99', 'R14', 'L82'], 7),
])

# 2359 is too low
# 8101 is too high

lines = read_lines_while_not_empty()
print_list(lines, 'Input')
print(f'Amount of zeros: {solve(lines)}')
