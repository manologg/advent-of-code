#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readlines():
    return [line[:-1].replace(' ', '') for line in input_file.readlines()]


OPERATIONS = {
    '+': int.__add__,
    '*': int.__mul__
}

NUMBER = 'N'
OPERATOR = 'O'


def evaluate(line):
    first = line[0]
    line = line[1:]
    parsed = 1

    if first.isdigit():
        parsing_number = first
        parsed_operation = None
        last = NUMBER
    elif first in OPERATIONS.keys():
        parsing_number = None
        parsed_operation = OPERATIONS[first]
        last = OPERATOR
    elif first == '(':
        parsing_number, parsed_chars = evaluate(line)
        parsed_operation = None
        line = line[parsed_chars:]
        parsed += parsed_chars
        last = NUMBER
    else:
        raise Exception('Unexpected char \'{}\' at the beginning'.format(first))

    result = None

    while line:

        current = line[0]
        line = line[1:]
        parsed += 1

        if last == NUMBER:
            if current.isdigit():
                parsing_number += current
            elif current in OPERATIONS.keys():
                if parsed_operation:
                    result = parsed_operation(result, int(parsing_number))
                else:
                    result = int(parsing_number)
                parsed_operation = OPERATIONS[current]
                parsing_number = None
                last = OPERATOR
            elif current == ')':
                return parsed_operation(result, int(parsing_number)), parsed
            else:
                raise Exception('Not known character: \'{}\''.format(current))
        elif last == OPERATOR:
            if current.isdigit():
                parsing_number = current
                last = NUMBER
            elif current == '(':
                parsing_number, parsed_chars = evaluate(line)
                line = line[parsed_chars:]
                parsed += parsed_chars
                last = NUMBER
            else:
                raise Exception('Not known character: {}'.format(current))
        else:
            raise Exception('Not known last state: {}'.format(last))

    if last == NUMBER:
        return parsed_operation(result, int(parsing_number)), parsed
    else:
        raise Exception('It doesn\'t make sense to have 2 contiguous operators. Second one:: {}'.format(line[-1]))


def test(test_cases):
    for line, expected in test_cases:
        result, parsed = evaluate(line.replace(' ', ''))
        if result == expected:
            print('{} --> OK'.format(line))
        else:
            raise AssertionError('Expected: {}. Found: {}'.format(expected, result))
    print('All tests passed!')


test([
    ('1 + 2 * 3 + 4 * 5 + 6', 71),
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 26),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
])

lines = readlines()
print(lines)
total = sum([evaluate(line)[0] for line in lines])
print('Total:', total)
