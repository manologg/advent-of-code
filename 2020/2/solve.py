#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def is_valid(first, second, character, password):
    print('first: {} second: {} character: {} password: \'{}\''.format(first, second, character, password))

    first_c = password[int(first)-1]
    second_c = password[int(second)-1]
    return (first_c == character and second_c != character) or (first_c != character and second_c == character)


line = readline()
valid_passwords = 0
while line:

    match = re.match(r'(?P<first>\d+)-(?P<second>\d+) (?P<character>\w): (?P<password>\w+)', line)
    if is_valid(**match.groupdict()):
        valid_passwords += 1

    line = readline()

print('Valid passwords: {}'.format(valid_passwords))
