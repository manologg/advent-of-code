#!/usr/bin/python
# coding=utf-8
import re
from itertools import count

input_file = open('input.txt')


def read_int_lines():
    return [int(x[:-1]) for x in input_file.readlines()]


def transform(value, subject_number):
    return (value * subject_number) % 20201227


def find_loop_size(subject_number, public_key):
    value = 1
    for loop_size in count(start=1, step=1):
        value = transform(value, subject_number)
        if value == public_key:
            return loop_size


def generate_key(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = transform(value, subject_number)
    return value


def test(test_cases):
    for func, subject_number, public_key, expected in test_cases:
        result = func(subject_number, public_key)
        if result == expected:
            print(f'{func.__name__}({subject_number, public_key}) --> OK')
        else:
            raise AssertionError('Expected: {}. Found: {}'.format(expected, result))
    print('All tests passed!')


test([
    (find_loop_size, 7, 5764801, 8),
    (find_loop_size, 7, 17807724, 11),
    (generate_key, 17807724, 8, 14897079),
    (generate_key, 5764801, 11, 14897079),
])


card_public_key, door_public_key = read_int_lines()
print(f'{card_public_key=}, {door_public_key=}')

card_loop_size = find_loop_size(7, card_public_key)
door_loop_size = find_loop_size(7, door_public_key)
print(f'{card_loop_size=}, {door_loop_size=}')

card_private_key = generate_key(card_public_key, door_loop_size)
door_private_key = generate_key(door_public_key, card_loop_size)
print(f'{card_private_key=}, {door_private_key=}')

