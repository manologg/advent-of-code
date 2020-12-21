#!/usr/bin/python
# coding=utf-8
from copy import copy, deepcopy
from time import sleep

input_file = open('input.txt')

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def readlines():
    return [[c for c in x[:-1]] for x in input_file.readlines()]


def print_map(map):
    print()
    for row in map:
        print(' ', ''.join(row))
    print()


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]


def get_cell(map, i, j, direction):
    new_i = i + direction[0]
    new_j = j + direction[1]
    if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]):
        return None
    return map[new_i][new_j]


def is_first_seat_in_direction_occupied(map, i, j, direction):
    cell = get_cell(map, i, j, direction)

    if cell is None:
        # we are at the end of the map --> no occupied seat
        return False

    elif cell == FLOOR:
        # we still need to look into that direction to see if there's something there
        return is_first_seat_in_direction_occupied(map, i + direction[0], j + direction[1], direction)

    else:  # cell in [EMPTY, OCCUPIED]
        # we found something --> check if it's occupied
        return cell == OCCUPIED


def count_occupied_seats(map, i, j):
    occupied_seats = 0
    for direction in DIRECTIONS:
        if is_first_seat_in_direction_occupied(map, i, j, direction):
            occupied_seats += 1

    return occupied_seats


def step(map):
    new_map = deepcopy(map)
    changes = 0

    for i, row in enumerate(map):
        for j, seat in enumerate(row):

            if seat == FLOOR:
                continue

            occupied_seats = count_occupied_seats(map, i, j)

            if seat == EMPTY and not occupied_seats:
                new_map[i][j] = OCCUPIED
                changes += 1
            elif seat == OCCUPIED and occupied_seats >= 5:
                new_map[i][j] = EMPTY
                changes += 1

    return new_map, changes


def step_until_stale(map):
    t = 0
    print('t=0')
    print_map(map)
    while True:
        t += 1
        map, changes = step(map)
        print('----------------')
        print()
        print('t={} ({} changes)'.format(t, changes))
        print_map(map)
        if not changes:
            return map


map = readlines()
map = step_until_stale(map)
occupied_seats = sum([sum([1 if seat == OCCUPIED else 0 for seat in row]) for row in map])
print('Occupied seats:', occupied_seats)
