#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


################################################################

def readline():
    return input_file.readline()[:-1]


def ignore_line():
    line = readline()
    print('ignoring line \'{}\'', line)


def parse(line):
    match = re.match(r'(?P<key>\w+): (?P<value>\w+)', line).groupdict()
    return int(match['key']), int(match['value'])


def readlines():
    line = readline()
    x = []
    while line:
        x.append(parse(line))
        line = readline()
    return x


################################################################


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


################################################################


def test(test_cases):
    for line, expected in test_cases:
        result, parsed = evaluate(line.replace(' ', ''))
        if result == expected:
            print('{} --> OK'.format(line))
        else:
            raise AssertionError('Expected: {}. Found: {}'.format(expected, result))
    print('All tests passed!')


x = readlines()
print(x)
