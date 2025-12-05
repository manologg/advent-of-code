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


def print_solution(solution):
    print(f'Solution: {solution}')


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


def read_comma_separated_line():
    return [range.split('-') for range in read_line().split(',')]


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def invalid(i):
    s = str(i)
    l = len(s)
    middle = l // 2
    return l % 2 == 0 and s[:middle] == s[middle:]


def invalid_ids(ids_range):
    for i in range(int(ids_range[0]), int(ids_range[1]) + 1):
        if invalid(i):
            yield i


def solve(ids_list):
    all_invalid_ids = []
    for ids_range in ids_list:
        all_invalid_ids.extend(invalid_ids(ids_range))
    return sum(all_invalid_ids)


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
    (
        [
            ['11', '22'],
        ],
        33
    ),
    (
        [
            ['11', '22'],
            ['95', '115'],
        ],
        243
    ),
    (
        [
            ['11', '22'],
            ['95', '115'],
            ['998', '1012'],
            ['1188511880', '1188511890'],
            ['222220', '222224'],
            ['1698522', '1698528'],
            ['446443', '446449'],
            ['38593856', '38593862'],
            ['565653', '565659'],
            ['824824821', '824824827'],
            ['2121212118', '2121212124'],
        ],
        4174379265
    ),
])

line = read_comma_separated_line()
print_list(line, 'Input')
result = solve(line)
print_solution(result)
