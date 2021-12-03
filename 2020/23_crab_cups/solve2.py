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


def find_destination(cups, dest, pickup, cache):
    while dest in pickup:
        dest -= 1
    try:
        return cache[dest]

    except KeyError:
        while True:
            if dest == 0:
                dest = max(cups)
            try:
                return cups.index(dest)
            except ValueError:
                dest -= 1


def update_cache(cache, position):

    # change cache entries after first ones
    for x, i in blist(cache.items()):
        if i > position:
            cache[x] = i - 3


# def sum_to_cache(cache, from_a, amount_a, from_b, amount_b):
#     for x, i in cache.items():
#         if i >= from_a:
#             cache[x] = i + amount_a
#         if i >= from_b:
#             cache[x] = i + amount_b


def get_slice(cups, start, end):
    return cups[start:end] + cups[:max(end - len(cups), 0)]


def get_three(cups, i):
    for _ in range(3):
        try:
            yield cups.pop(i)
        except IndexError:
            i = 0
            yield cups.pop(i)


def move(cups, cache, current_i):

    current = cups[current_i]
    first, second, third = get_three(cups, current_i + 1)

    update_cache(cache, current_i + 1)
    dest_i = find_destination(cups, current - 1, [first, second, third], cache)

    cups.insert(dest_i + 1, first)
    cups.insert(dest_i + 2, second)
    cups.insert(dest_i + 3, third)

    current_i = current_i if dest_i > current_i else current_i + 3
    next_i = current_i + 1 if current_i + 1 < len(cups) else 0

    return {
        first: dest_i + 1,
        second: dest_i + 2,
        third: dest_i + 3,
        current: current_i,
    }, next_i


def play(cups, moves, current_i=0, return_only_2=False):  # last param is only for part 2

    cups = blist(cups)
    cache = dict()

    for i in range(1, moves + 1):
        cache, current_i = move(cups, cache, current_i)
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
    for cups, moves, expected in test_cases:
        result = play(cups, moves)
        if result == expected:
            print(f'({cups=}, {moves=}) --> OK')
        else:
            raise AssertionError(f'Expected: {expected}. Found: {result}')
    print('All tests passed!')
    print()


test([
    ([3, 8, 9, 1, 2, 5, 4, 6, 7], 10, '92658374'),
    ([3, 8, 9, 1, 2, 5, 4, 6, 7], 100, '67384529'),
])

# cups = read_cups()
cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
print(f'{cups=}')

cups = more_cups(cups, up_to=1000000)
labels_after_1 = run_with_profiling(play, cups, moves=100, return_only_2=True)
print()
print(f'First two labels multiplied: {int(labels_after_1[0]) * int(labels_after_1[1])}')
