#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def print_title(title):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def parse(line):
    tiles = []
    while line:
        x = line.pop(0)
        if x in ['e', 'w']:
            tiles.append(x)
        elif x in ['n', 's']:
            tiles.append(x + line.pop(0))
    return tiles


def read_and_parse_lines():
    return [parse([x for x in line[:-1]]) for line in input_file.readlines()]


def move(x, y, z, command):
    if command == 'w':
        x -= 1
        y += 1
    elif command == 'e':
        x += 1
        y -= 1
    elif command == 'nw':
        y += 1
        z -= 1
    elif command == 'se':
        y -= 1
        z += 1
    elif command == 'ne':
        x += 1
        z -= 1
    elif command == 'sw':
        x -= 1
        z += 1
    else:
        raise Exception(f'Unknown command {command}')

    return x, y, z

def navigate(path):
    x = y = z = 0
    for command in path:
        x, y, z = move(x, y, z, command)
    return x, y, z


def flip_tiles(paths):
    black_tiles = set()
    for path in paths:
        coordinates = navigate(path)
        if coordinates in black_tiles:
            black_tiles.remove(coordinates)
        else:
            black_tiles.add(coordinates)
    return black_tiles


def get_adjacent(x, y, z, black_tiles):
    adjacent = set([move(x, y, z, command) for command in ['w', 'e', 'nw', 'se', 'ne', 'sw']])
    return adjacent.intersection(black_tiles), adjacent - black_tiles


def step(black_tiles):

    # black tiles
    all_white_adjacent_tiles = set()
    new_black_tiles = set()
    for tile in black_tiles:
        black, white = get_adjacent(*tile, black_tiles)
        if len(black) in [1, 2]:  # only the ones with 0 or more than 2 become white
            new_black_tiles.add(tile)
        all_white_adjacent_tiles.update(white)

    # white tiles
    for tile in all_white_adjacent_tiles:
        black, white = get_adjacent(*tile, black_tiles)
        if len(black) == 2:
            new_black_tiles.add(tile)

    return new_black_tiles


def conway_tiles(black_tiles, days):
    for day in range(1, days+1):
        black_tiles = step(black_tiles)

    return black_tiles


paths = read_and_parse_lines()

# part 1
black_tiles = flip_tiles(paths)
print(f'Black tiles - day 0: {len(black_tiles)}')

# part 2
black_tiles = conway_tiles(black_tiles, days=100)
print(f'Black tiles - day 100: {len(black_tiles)}')
