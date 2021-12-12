#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def solve(lines):
    increases = 0
    last = lines[0]
    for n in lines[1:]:
        if n > last:
            increases += 1
        last = n

    return increases


lines = read_int_lines()
increases = solve(lines)
print(f'{increases} increases')