#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return [int(x) for x in input_file.readline()[:-1].split(',')]


def play(numbers, end):

    numbers_dict = {n: i+1 for i, n in enumerate(numbers[:-1])}
    last = numbers[-1]
    for i in range(len(numbers), end):
        pos = numbers_dict.get(last)
        numbers_dict[last] = i
        if pos is None:
            last = 0
        else:
            last = i - pos
    return last


def test(numbers, end, expected_result):
    result = play(numbers, end)
    assert result == expected_result


test([0, 3, 6], 2020, 436)
test([1, 3, 2], 2020, 1)
test([2, 1, 3], 2020, 10)
test([1, 2, 3], 2020, 27)
test([2, 3, 1], 2020, 78)
test([3, 2, 1], 2020, 438)
test([3, 1, 2], 2020, 1836)

numbers = readline()
print(numbers)
result = play(numbers, 30000000)
print('30000000th number:', result)
