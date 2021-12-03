#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


################################################################

def readline():
    return input_file.readline()[:-1]


def ignore_line():
    line = readline()
    print('ignoring line \'{}\'', line)


def readlines():
    line = readline()
    x = []
    while line:
        x.append(line)
        line = readline()
    return x


################################################################


def readlines():
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
