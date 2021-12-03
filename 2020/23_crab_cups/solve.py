#!/usr/bin/python
# coding=utf-8
import cProfile
import io
from collections import OrderedDict
from copy import deepcopy
from pstats import SortKey, Stats
from blist import blist, sorteddict

input_file = open('input.txt')


def run_with_profiling(func, *args, **kwargs):
    profile = cProfile.Profile()
    profile.enable()

    # run the code
    result = func(*args, **kwargs)

    profile.disable()
    stream = io.StringIO()
    sort_by = SortKey.CUMULATIVE
    stats = Stats(profile, stream=stream).sort_stats(sort_by)
    stats.print_stats()
    print(stream.getvalue())

    return result


def read_cups():
    return [int(x) for x in input_file.readline()[:-1]]


def more_cups(cups, up_to):
    return cups + [x for x in range(max(cups) + 1, up_to + 1)]


def find_destination(cups, dest, cache):
    try:
        return cache[dest]

    except KeyError:
        while True:
            if dest == 0:
                dest = max(cups)
            try:
                print(f'index of {dest}!')
                return cups.index(dest)
            except ValueError:
                dest -= 1


def invalidate_first_elements_in_cache(cache, deleted):

    how_many = len(deleted)

    to_be_deleted = []

    # change cache entries after first ones
    for x, i in blist(cache.items()):
        if i < how_many:
            to_be_deleted.append(x)
        else:
            cache[x] = i - how_many

    # delete first ones
    for x in to_be_deleted:
        del cache[x]


# def sum_to_cache(cache, from_a, amount_a, from_b, amount_b):
#     for x, i in cache.items():
#         if i >= from_a:
#             cache[x] = i + amount_a
#         if i >= from_b:
#             cache[x] = i + amount_b


def move(cups, cache, last_i):
    slice = cups[0:4]
    current, first, second, third = slice

    invalidate_first_elements_in_cache(cache, slice)
    del cups[0:4]
    dest_i = find_destination(cups, current - 1, cache)

    cups.insert(dest_i + 1, first)
    cups.insert(dest_i + 2, second)
    cups.insert(dest_i + 3, third)
    cups.insert(last_i, current)

    return cups, {
        first: dest_i + 1,
        second: dest_i + 2,
        third: dest_i + 3,
        current: last_i,
    }


def play(cups, moves, return_only_2=False):  # last param is only for part 2

    last_i = len(cups) - 1
    cups = blist(cups)
    cache = dict()

    for i in range(1, moves + 1):
        cups, cache = move(cups, cache, last_i)
        # if i % 1000 == 0:
        #     print(i)

    print(f'Cache size: {len(cache.keys())}')

    one_i = cups.index(1)
    cups_without_one = [str(x) for x in cups[one_i + 1:] + cups[:one_i]]
    if return_only_2:
        return cups_without_one[:2]
    else:
        return ''.join(cups_without_one)


def test(test_cases):
    for cups, moves,aa expected in test_cases:
        result = play(cups, moves)
        if result == expectaaed:
            print(f'({cups=}, {moves=}) --> OK')
        else:
            raise AssertionError(f'Expected: {expected}. Found: {result}')
    print('All tests passed!')
    print()


# test([
#     ([3, 8, 9, 1, 2, 5, 4, 6, 7], 10, '92658374'),
#     ([3, 8, 9, 1, 2, 5, 4, 6, 7], 100, '67384529'),
# ])

# cups = read_cups()
cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
print(f'{cups=}')

cups = more_cups(cups, up_to=100)
labels_after_1 = run_with_profiling(play, cups, moves=100, return_only_2=True)
print()
print(f'First two labels multiplied: {int(labels_after_1[0]) * int(labels_after_1[1])}')
