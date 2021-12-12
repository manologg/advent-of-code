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


POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

END_OF = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def check(chunk):
    first = chunk[0]
    chunk = chunk[1:]

    while chunk[0] in END_OF.keys():
        chunk = check(chunk)
    
    next = chunk[0]
    if next != END_OF[first]:
        print(f'Expected {END_OF[first]}, but found {next} instead')
        raise ValueError(next)

    return chunk[1:]


def solve(lines):
    points = 0
    for i, line in enumerate(lines):
        print(line)
        try:
            check(line)
            print(f'0 points for line {i} (ok)')
        except ValueError as e:
            print(f'{POINTS[e.args[0]]} points for line {i}')
            points += POINTS[e.args[0]]
        except IndexError:
            print(f'0 points for line {i} (incomplete line)')

        print()
    return points


lines = read_lines()
points = solve(lines)
print(f'Total syntax error score: {points}')
