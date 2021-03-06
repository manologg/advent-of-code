#!/usr/bin/python
# coding=utf-8
from copy import deepcopy
from itertools import product

input_file = open('input.txt')
all_lines = input_file.readlines()

ACTIVE = '#'
INACTIVE = '.'
ORIGINAL_SIZE = len(all_lines)
CYCLES = 6
EXPANDED_SIZE = ORIGINAL_SIZE + CYCLES * 2


def new_row():
    return [INACTIVE for _ in range(EXPANDED_SIZE)]


def new_half_row():
    return [INACTIVE for _ in range(CYCLES)]


def new_floor():
    return [new_row() for _ in range(EXPANDED_SIZE)]


def new_half_floor():
    return [new_row() for _ in range(CYCLES)]


def readlines():
    return [new_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_half_floor() + [
                new_half_row()
                + [c for c in x[:-1]]
                + new_half_row() for x in all_lines
            ] + new_half_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_floor(),
            new_floor()]


def print_map(t, map):
    print()
    print(' t={}'.format(t))
    print('-----')
    for z, floor in enumerate(map):
        if sum([sum([1 if cube == ACTIVE else 0 for cube in row]) for row in floor]) > 0:
            print('z={}'.format(z - CYCLES))
            for row in floor:
                print(''.join(row))
            print()
    print()


DIRECTIONS = [x for x in product([-1, 0, 1], repeat=3)]
DIRECTIONS.remove((0, 0, 0))


def get_cube(map, z, y, x, direction):
    new_z = z + direction[0]
    new_y = y + direction[1]
    new_x = x + direction[2]
    if new_z < 0 or new_z >= len(map)\
            or new_y < 0 or new_y >= len(map[0])\
            or new_x < 0 or new_x >= len(map[0][0]):
        return INACTIVE
    return map[new_z][new_y][new_x]


def count_active_neighbours(map, z, y, x):
    active_neighbours = 0
    for direction in DIRECTIONS:
        if get_cube(map, z, y, x, direction) == ACTIVE:
            active_neighbours += 1
    return active_neighbours


def step(map):
    new_map = deepcopy(map)

    for z, floor in enumerate(map):
        for y, row in enumerate(floor):
            for x, cube in enumerate(row):

                active_neighbors = count_active_neighbours(map, z, y, x)

                if cube == ACTIVE and active_neighbors not in [2, 3]:
                    new_map[z][y][x] = INACTIVE
                elif cube == INACTIVE and active_neighbors == 3:
                    new_map[z][y][x] = ACTIVE

    return new_map


def run(map, cycles):
    print_map(0, map)
    for t in range(1, cycles + 1):
        map = step(map)
        print('----------------')
        print_map(t, map)
    return map


map = readlines()
map = run(map, cycles=6)
active_cubes = sum([sum([sum([1 if cube == ACTIVE else 0 for cube in row]) for row in floor]) for floor in map])
print('Active cubes:', active_cubes)
