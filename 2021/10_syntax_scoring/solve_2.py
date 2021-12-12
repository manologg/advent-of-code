#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def read_lines():
    return [x[:-1] for x in input_file.readlines()]


END_OF = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def flip_and_convert(chars):
    return ''.join([END_OF[c] for c in chars[::-1]])


def check(chunk, openings=None):

    if not openings:
        openings = []

    first = chunk[0]
    chunk = chunk[1:]

    try:
        while chunk[0] in END_OF.keys():
            chunk = check(chunk, openings + [first])
    except IndexError:
        raise ValueError(flip_and_convert(openings + [first]))
    
    next = chunk[0]
    if next != END_OF[first]:
        # print(f'Expected {END_OF[first]}, but found {next} instead')
        raise Warning()

    return chunk[1:]


POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def calculate_points(chars):
    points = 0
    for c in chars:
        points *= 5
        points += POINTS[c]

    return points


def solve(lines):
    points = []
    for i, line in enumerate(lines):
        # print(line)
        try:
            while line:
                line = check(line)
            print(f'0 points for line {i} (ok)')
        except Warning:
            # print(f'0 points for line {i} (corrupted line)')
            pass
        except ValueError as e:
            line_points = calculate_points(e.args[0])
            print(line)
            print(f'{line_points} points for line {i}. Missing: {e.args[0]}')
            print()
            points.append(line_points)

    return points


lines = read_lines()
points = solve(lines)
print(f'Middle error score: {sorted(points)[len(points)//2]}')
