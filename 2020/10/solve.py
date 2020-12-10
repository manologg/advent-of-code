#!/usr/bin/python
# coding=utf-8
from functools import reduce

input_file = open('input.txt')


def readlines():
    return list(sorted([int(x[:-1]) for x in input_file.readlines()]))


def part(part):
    print()
    print('PART {}'.format(part))
    print('------')


def count_differences(numbers):
    one = 0
    three = 0
    last = numbers[0]
    for n in numbers[1:]:
        diff = n - last
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1
        else:
            raise Exception('Not valid! (diff={}, {} - {})'.format(diff, n, last))
        last = n

    return one, three


def analyze(numbers):
    ones = []
    consecutive_ones = 1
    last = numbers[0]
    for n in numbers[1:]:
        if n - last == 1:
            consecutive_ones += 1
        else:
            ones.append(consecutive_ones)
            consecutive_ones = 1
        last = n

    return [x for x in ones if x > 2]


def get_number_of_possible_changes(consecutive_digits):
    if consecutive_digits == 3:
        return 2
    elif consecutive_digits == 4:
        return 4
    elif consecutive_digits == 5:
        return 7
    else:
        raise Exception('not expected amount of consecutive digits')


def get_amount_of_possible_groups(analysis):
    """
    Every digit in the analysis contains the amount of digits that are consecutive (max. 5)
    """
    return reduce(lambda a, b: a * b, [get_number_of_possible_changes(x) for x in analysis])


numbers = readlines()
all_numbers = [0] + numbers + [max(numbers) + 3]
one, three = count_differences(all_numbers)

part(1)
print('There are {} differences of 1 jolt and {} differences of 3 jolts.'.format(one, three))
print('Both multiplied: {}'.format(one * three))

part(2)
analysis = analyze(all_numbers)
print('All numbers: ', all_numbers)
print('Groups of consecutive numbers: ', analysis)
print('Possibilities: {}'.format(get_amount_of_possible_groups(analysis)))
