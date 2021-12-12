#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def print_simple_list(l, title):
    print(f'{title}: {",".join([str(x) for x in l])}')


def parse(line):
    groupdict = re.match(r'^(?P<from>\w+)-(?P<to>\w+)$', line).groupdict()
    return groupdict['from'], groupdict['to']


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def get_destinations(cave, paths):
    destination_caves = {dst for _, dst in paths if (cave, dst) in paths}
    source_caves = {src for src, _ in paths if (src, cave) in paths}
    return destination_caves.union(source_caves)


def group_paths(paths):
    all_caves = {src for src, _ in paths}.union({dst for _, dst in paths})
    return {cave: get_destinations(cave, paths) for cave in all_caves}


def small_caves(caves):
    return [cave for cave in caves if cave.islower() and cave not in ['start', 'end']]


def navigate(paths, repeat, current='start', visited=None):
    if not visited:
        visited = []

    if current in visited and current.islower():
        # was visited once, not anymore
        if current == repeat:
            repeat = None
        else:
            return []

    if current == 'end':
        all_visited = '-'.join(visited + [current])
        print(f'Path: {all_visited}')
        return [all_visited]

    all_paths = []
    for cave in paths[current]:
        all_paths.extend(navigate(paths, repeat=repeat, current=cave, visited=visited + [current]))

    return all_paths


lines = read_and_parse_lines()
paths = group_paths(lines)
print_list(paths.items(), 'Paths')
print()
all_paths = []
for small_cave in small_caves(paths.keys()):
    all_paths.extend(navigate(paths, repeat=small_cave))

print(f'Amount of possible paths through the cave system: {len(set(all_paths))}')
