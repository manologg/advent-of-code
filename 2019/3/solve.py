#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    line = input_file.readline()[:-1]
    return [(x[0], int(x[1:])) for x in line.split(',')]


def follow(wire, visited, visited_steps, steps, x, y):

    if not wire:
        return visited, visited_steps

    direction = wire[0][0]
    length = wire[0][1]

    new_x = x
    new_y = y

    if direction == 'R':
        new_x = x + length
        for c, i in enumerate(range(x + 1, new_x + 1)):
            visited.append((i, y))
            visited_steps['{},{}'.format(i, y)] = steps + c + 1
    if direction == 'L':
        new_x = x - length
        for c, i in enumerate(range(x - 1, new_x - 1, -1)):
            visited.append((i, y))
            visited_steps['{},{}'.format(i, y)] = steps + c + 1
    if direction == 'U':
        new_y = y + length
        for c, j in enumerate(range(y + 1, new_y + 1)):
            visited.append((x, j))
            visited_steps['{},{}'.format(x, j)] = steps + c + 1
    if direction == 'D':
        new_y = y - length
        for c, j in enumerate(range(y - 1, new_y - 1, -1)):
            visited.append((x, j))
            visited_steps['{},{}'.format(x, j)] = steps + c + 1

    return follow(wire[1:], visited, visited_steps, steps + length, new_x, new_y)


first = readline()
second = readline()

visited_first, steps_first = follow(first, [], {}, 0, 0, 0)
visited_second, steps_second = follow(second, [], {}, 0, 0, 0)

visited_both = set(visited_first).intersection(set(visited_second))
steps = [steps_first['{},{}'.format(x, y)] + steps_second['{},{}'.format(x, y)] for x, y in visited_both]
print(min(steps))
