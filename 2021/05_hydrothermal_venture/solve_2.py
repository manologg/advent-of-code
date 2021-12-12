#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_title(title):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)
    print()


def print_lines(l, title=''):
    print_title(title)
    for x1, y1, x2, y2 in l:
        print(f'({x1}, {y1}) -> ({x2}, {y2})')


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print(f'{key}: {value}')


def parse(line):
    groupdict = re.match(r'^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$', line).groupdict()
    _ = lambda x: int(groupdict[x])
    return _('x1'), _('y1'), _('x2'), _('y2')


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def mark_point(x, y, points):
    try:
        points[(x, y)] += 1
    except KeyError:
        points[(x, y)] = 1


incr = lambda x: x + 1
decr = lambda x: x - 1
noop = lambda x: x


def get_op(x1, x2):
    return noop if x1 == x2 else incr if x1 < x2 else decr


def mark_line(x1, y1, x2, y2, points):

    x_op = get_op(x1, x2)
    y_op = get_op(y1, y2)
    # print(f'x_op: {x_op}')
    # print(f'y_op: {y_op}')
    x = x1
    y = y1
    amount_of_points = abs(x1 - x2) if y1 == y2 else abs(y1 - y2)
    for _ in range(amount_of_points + 1):
        mark_point(x, y, points)
        x = x_op(x)
        y = y_op(y)


def solve(lines):
    points = {}

    for line in lines:
        x1, y1, x2, y2 = line
        mark_line(x1, y1, x2, y2, points)
        # print(f'Line: ({x1}, {y1}) -> ({x2}, {y2})')
        # print_map(points)

    return points


def print_map(points):
    print('Map:')
    for y in range(10):
        line = ''
        for x in range(10):
            if (x, y) in points:
                line += f'{points[(x,y)]}'
            else:
                line += '.'
        print(line)
    print()


lines = read_and_parse_lines()
# print_lines(lines, 'Lines')
points = solve(lines)
# print_map(points)
print(f'Amount of points where at least 2 lines overlap: {sum([1 for i in points.values() if i > 1])}')
