#!/usr/bin/python
# coding=utf-8
import re
from collections import namedtuple

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
    for x in l:
        print(f'({x.x1}, {x.y1}) -> ({x.x1}, {x.y1})')


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print(f'{key}: {value}')


def parse(line):
    groupdict = re.match(r'^(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)$', line).groupdict()
    Line = namedtuple('Line', 'x1 y1 x2 y2')
    return Line(int(groupdict['x1']), int(groupdict['y1']), int(groupdict['x2']), int(groupdict['y2']))


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def mark_point(x, y, points):
    try:
        points[f'{x},{y}'] += 1
    except KeyError:
        points[f'{x},{y}'] = 1


def mark_line(line, points):

    # horizontal lines
    if line.x1 == line.x2:
        a = min(line.y1, line.y2)
        b = max(line.y1, line.y2)
        for i in range(a, b + 1):
            mark_point(line.x1, i, points)

    # vertical lines
    if line.y1 == line.y2:
        a = min(line.x1, line.x2)
        b = max(line.x1, line.x2)
        for i in range(a, b + 1):
            mark_point(i, line.y1, points)


def solve(lines):
    points = {}

    for line in lines:
        mark_line(line, points)
        # print(f'Line: ({line.x1}, {line.y1}) -> ({line.x2}, {line.y2})')
        # print_list(points.items(), 'Covered points')

    return points


lines = read_and_parse_lines()
print_lines(lines, 'Lines')
points = solve(lines)
print(f'Amount of points where at least 2 lines overlap: {sum([1 for i in points.values() if i > 1])}')
