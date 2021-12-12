#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print(f'ignoring line \'{line}\'')


def get_digit_sets(numbers):
    return [set(x) for x in numbers.split(' ')]


def get_digit_strs(numbers):
    return [''.join(sorted(x)) for x in numbers.split(' ')]


def parse(line):
    groupdict = re.match(r'^(?P<input>[a-g ]+) \| (?P<output>[a-g ]+)$', line).groupdict()
    return get_digit_sets(groupdict['input']), get_digit_strs(groupdict['output'])


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


"""
DIGITS:

1: c f              (len = 2)
7: a c f            (len = 3)
4: b c d f          (len = 4)
8: a b c d e f g    (len = 7)

2: a c d e g        (len = 5)
3: a c d f g        (len = 5)
5: a b d f g        (len = 5)

0: a b c e f g      (len = 6)
6: a b d e f g      (len = 6)
9: a b c d f g      (len = 6)
"""


def first_str_with_len(numbers, expected_len):
    return next(filter(lambda s: len(s) == expected_len, numbers))


def find_three(numbers, one):
    return next(filter(lambda s: len(s) == 5 and one.issubset(s), numbers))


def find_five(numbers, one, four):
    difference = four - one
    return next(filter(lambda s: len(s) == 5 and difference.issubset(s), numbers))


def find_two(numbers, three, five):
    return next(filter(lambda s: len(s) == 5 and s != three and s != five, numbers))


def find_nine(numbers, four):
    return next(filter(lambda s: len(s) == 6 and four.issubset(s), numbers))


def find_zero(numbers, one, nine):
    return next(filter(lambda s: len(s) == 6 and one.issubset(s) and s != nine, numbers))


def find_six(numbers, zero, nine):
    return next(filter(lambda s: len(s) == 6 and s != zero and s != nine, numbers))


def _(digit):
    return ''.join(sorted(digit))


def get_digits(numbers):
    one = first_str_with_len(numbers, 2)
    seven = first_str_with_len(numbers, 3)
    four = first_str_with_len(numbers, 4)
    eight = first_str_with_len(numbers, 7)

    three = find_three(numbers, one)
    five = find_five(numbers, one, four)
    two = find_two(numbers, three, five)

    nine = find_nine(numbers, four)
    zero = find_zero(numbers, one, nine)
    six = find_six(numbers, zero, nine)

    return {
        _(zero): 0,
        _(one): 1,
        _(two): 2,
        _(three): 3,
        _(four): 4,
        _(five): 5,
        _(six): 6,
        _(seven): 7,
        _(eight): 8,
        _(nine): 9,
    }


def solve(lines):
    total = 0
    for input, output in lines:
        digits = get_digits(input)
        value = [str(digits[n]) for n in output]
        total += int(''.join(value))

    return total


lines = read_and_parse_lines()
total = solve(lines)
print(f'Sum of all output values: {total}')
