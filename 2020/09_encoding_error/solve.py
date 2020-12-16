#!/usr/bin/python
# coding=utf-8
from itertools import combinations

input_file = open('input.txt')


def readlines():
    return [int(x[:-1]) for x in input_file.readlines()]


def both_sum_n(n, numbers):
    for x, y in combinations(numbers, 2):
        if x + y == n:
            return True
    return False


def check_xmas(numbers, preamble_length):
    for i, n in enumerate(numbers[preamble_length:], preamble_length):
        previous_numbers = numbers[i - preamble_length:i]
        # print('n: %s' % n)
        # print('previous numbers: %s' % previous_numbers)
        comb_numbers = combinations(previous_numbers, 2)
        if not both_sum_n(n, previous_numbers):
            return n
        # print('---------------')


def find_sum(numbers, goal):
    # print('Trying to find sum in %s (goal: %s)' % (numbers, goal))
    sum = 0
    for i, n in enumerate(numbers, 1):
        sum += n
        if sum == goal:
            return True, i
    return False, None


def find_contiguous_numbers(numbers, n):
    for i in range(len(numbers)):
        found, offset = find_sum(numbers[i:], n)
        if found:
            print('Found sum: %s sum up to %s' % (numbers[i:i+offset], n))
            return numbers[i:i+offset]
    raise Exception('No contiguous numbers found that add up to %s' % n)


numbers = readlines()
n = check_xmas(numbers, 25)
print('Numbers: %s' % numbers)
print('First number that does not comply XMAS specification: %s' % n)
cont_numbers = find_contiguous_numbers(numbers, n)
print('Smallest and largest number added: %s' % (min(cont_numbers) + max(cont_numbers)))
