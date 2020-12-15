#!/usr/bin/python
# coding=utf-8
from itertools import count

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def readlines():
    return int(readline()), [int(x) for x in readline().split(',') if x != 'x']


def get_min_waiting_bus(arrival_time, buses):
    buses_with_waiting_time = [(x, x - (arrival_time % x)) for x in buses]
    return min(buses_with_waiting_time, key=lambda x: x[1])


def read_second_line():
    _ = input_file.readline()
    return [x if x == 'x' else int(x) for x in readline().split(',')]


# PART 1
# arrival_time, buses = readlines()
# print('arrival time:', arrival_time)
# print('buses:', buses)
# bus_id, waiting_time = get_min_waiting_bus(arrival_time, buses)
# print('ID of the earliest bus multiplied by the number of minutes:', bus_id * waiting_time)

def check_timestamp(timestamp, buses, reference_bus_offset):
    for i, bus in buses:
        if (timestamp + i) % bus != 0:
            return False

    print('This is the good one:', timestamp - reference_bus_offset)
    return True


def enumerate_buses(buses):
    enumerated_buses = [x for x in enumerate(buses) if x[1] != 'x']
    reference_bus = max(enumerated_buses, key=lambda x: x[1])
    return reference_bus, [(x[0] - reference_bus[0], x[1]) for x in enumerated_buses if x != reference_bus]


def find_earliest_timestamp(buses, start=0):
    reference_bus, enumerated_buses = enumerate_buses(buses)
    enumerated_buses = sorted(enumerated_buses, key=lambda x: x[1], reverse=True)
    print('Reference bus:', reference_bus)
    print('Enumerated buses:', enumerated_buses)
    for timestamp in count(start=start, step=reference_bus[1]):

        found = True
        for i, bus in enumerated_buses:
            if (timestamp + i) % bus != 0:
                found = False
                break

        # if check_timestamp(timestamp, enumerated_buses, reference_bus[0]):
        if found:
            return timestamp - reference_bus[0]


def test(buses, expected):
    print('Buses:', buses)
    optimal_time = find_earliest_timestamp(buses)
    if optimal_time == expected:
        print('OK')
    else:
        print('NOPE!')
    print()


test([7, 13, 'x', 'x', 59, 'x', 31, 19], 1068781)
test([17, 'x', 13, 19], 3417)
test([67, 7, 59, 61], 754018)
test([67, 'x', 7, 59, 61], 779210)
test([67, 7, 'x', 59, 61], 1261476)
test([1789, 37, 47, 1889], 1202161486)

# PART 2
buses = read_second_line()
print('buses:', buses)
optimal_time = find_earliest_timestamp(buses, start=100000000000000)
print('Earliest timestamp:', optimal_time)
