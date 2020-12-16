#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def read_instructions():
    line = readline()
    instructions = []
    while line:
        instructions.append((line[0], int(line[1:])))
        line = readline()
    return instructions


DIRECTIONS = {
    0: lambda x, y: (x, y),
    90: lambda x, y: (y, -x),
    180: lambda x, y: (-x, -y),
    270: lambda x, y: (-y, x)
}


def turn_waypoint(waypoint, offset):
    angle = offset % 360
    operation = DIRECTIONS[angle]
    result = operation(*waypoint)
    return result


def move_ship(ship, waypoint, times):
    return ship[0] + waypoint[0] * times, \
           ship[1] + waypoint[1] * times


def move_waypoint(waypoint, direction, offset):
    x = waypoint[0]
    y = waypoint[1]

    if direction == 'N':
        y += offset
    elif direction == 'S':
        y -= offset
    elif direction == 'E':
        x += offset
    elif direction == 'W':
        x -= offset
    else:
        raise Exception('unknown direction')

    return x, y


def navigate(instructions, ship, waypoint):
    if not instructions:
        print('Nothing left to do')
        return ship

    i = instructions[0]
    command = i[0]
    offset = i[1]
    print('instruction: {}'.format(i))

    if command == 'L':
        waypoint = turn_waypoint(waypoint, -offset)
    elif command == 'R':
        waypoint = turn_waypoint(waypoint, offset)
    elif command == 'F':
        ship = move_ship(ship, waypoint, offset)
    else:
        waypoint = move_waypoint(waypoint, command, offset)

    print(' ↳ ship: {}, waypoint: {}'.format(ship, waypoint))
    print()

    return navigate(instructions[1:], ship, waypoint)


instructions = read_instructions()
print(instructions)
print()
print('ship: {}, waypoint: {}'.format((0, 0), (10, 1)))
print()
x, y = navigate(instructions, (0, 0), (10, 1))
d = abs(x) + abs(y)
print('-----------')
print('Navigated to ({},{})'.format(x, y))
print('Manhattan distance: {}'.format(d))
