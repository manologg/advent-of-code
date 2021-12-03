#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def solve(lines):
    increases = 0
    for i in range(3, len(lines)):
        last_sum = sum(lines[i-3:i])
        current_sum = sum(lines[i-2:i+1])
        if current_sum > last_sum:
            increases += 1

    return increases


lines = read_int_lines()
increases = solve(lines)
print(f'{increases} increases')