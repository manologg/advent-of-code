#!/usr/bin/python
# coding=utf-8
import re
from itertools import product

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def apply_mask_version_1(value, mask):
    bin_value = bin(value).split('b')[1][::-1]
    reversed_value = [x for x in bin_value] + ['0'] * (36 - len(bin_value))

    for position, new_value in mask:
        reversed_value[position] = new_value

    new_value = ''.join(reversed_value[::-1])
    return int(new_value, 2)


def apply_change(position, change):
    new_position = []
    bit = 0
    for x in position:
        if x in ['1', '0']:
            new_position.append(x)
        if x == 'X':
            new_position.append(change[bit])
            bit += 1
    return new_position


def create_all_positions_from_floating(position):
    positions = []
    amount_of_x = sum([1 for x in position if x == 'X'])
    all_changes = list(product('01', repeat=amount_of_x))
    for change in all_changes:
        positions.append(apply_change(position, change))

    return positions


def apply_mask_version_2(pos, mask):
    bin_position = bin(pos).split('b')[1][::-1]
    reversed_position = [x for x in bin_position] + ['0'] * (36 - len(bin_position))

    for pos, val in mask:
        if val == '0':
            pass
        elif val in ['1', 'X']:
            reversed_position[pos] = val
        else:
            raise Exception('Unexpected value in mask: {}'.format(val))

    positions = create_all_positions_from_floating(reversed_position[::-1])
    return [int(''.join(p), 2) for p in positions]


def parse_mask(line):
    mask = re.match(r'mask = (?P<mask>\w+)', line).groupdict()['mask']
    return [(35 - i, x) for i, x in enumerate(mask)]


def parse_mem(line):
    match = re.match(r'mem\[(?P<position>\w+)] = (?P<value>\d+)', line).groupdict()
    return int(match['position']), int(match['value'])


def write(mem, positions, value):
    for position in positions:
        mem[position] = value


line = readline()
mask = []
mem = {}

while line:
    if 'mask' in line:
        mask = parse_mask(line)
        print('mask:', mask)
        print()
    else:
        position, value = parse_mem(line)
        print('position:', position)
        positions = apply_mask_version_2(position, mask)
        print('positions:', positions)
        print()
        write(mem, positions, value)
    line = readline()

print('sum:', sum(mem.values()))
