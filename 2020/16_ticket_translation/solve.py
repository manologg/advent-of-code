#!/usr/bin/python
# coding=utf-8
import json
import re
from functools import reduce

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def ignore_line():
    _ = readline()


def get_range(groupdict, range_number):
    start = int(groupdict['start_{}'.format(range_number)])
    end = int(groupdict['end_{}'.format(range_number)]) + 1
    return list(range(start, end))


def read_fields():
    line = readline()
    fields = {}
    while line:
        match = re.match(r'(?P<field>[\w ]+): (?P<start_0>\d+)-(?P<end_0>\d+) or (?P<start_1>\d+)-(?P<end_1>\d+)', line)
        groupdict = match.groupdict()
        fields[groupdict['field']] = get_range(groupdict, 0) + get_range(groupdict, 1)
        line = readline()
    return fields


def parse_ticket(line):
    return [int(x) for x in line.split(',')]


def read_tickets():
    line = readline()
    tickets = []
    while line:
        tickets.append(parse_ticket(line))
        line = readline()
    return tickets


def get_valid_values(fields):
    valid_values = set()
    for field_name, values_list in fields.items():
        valid_values.update(values_list)
    return valid_values


def all_fields_are_valid(ticket, valid_values):
    for value in ticket:
        if value not in valid_values:
            return False
    return True


def read_input():
    fields = read_fields()

    # ignore one line
    ignore_line()

    # your ticket
    my_ticket = parse_ticket(readline())

    # ignore some more
    ignore_line()
    ignore_line()

    # nearby tickets
    tickets = read_tickets()

    valid_tickets = [x for x in tickets if all_fields_are_valid(x, get_valid_values(fields))]

    return fields, my_ticket, valid_tickets


def check_all_tickets(tickets, position, valid_values):
    for i, ticket in enumerate(tickets):
        if ticket[position] not in valid_values:
            return False
    return True


def find_positions(valid_values, tickets):
    positions = []
    for i in range(len(tickets[0])):
        valid_position = check_all_tickets(tickets, i, valid_values)
        if valid_position:
            positions.append(i)
    return positions


def find_structure(fields, tickets):
    return {name: find_positions(values, tickets) for name, values in fields.items()}


def refine_structure(field_structure, known_positions):
    possibilities = [len(x) for x in field_structure.values()]
    if sum(possibilities) == len(field_structure):
        return known_positions

    new_positions = {name: positions[0] for name, positions in field_structure.items() if len(positions) == 1}
    for name, position in new_positions.items():
        known_positions[name] = position
        del field_structure[name]

    for name, positions in field_structure.items():
        for i in new_positions.values():
            positions.remove(i)

    return refine_structure(field_structure, known_positions)


fields, my_ticket, valid_tickets = read_input()
field_structure = find_structure(fields, valid_tickets)
field_structure = refine_structure(field_structure, {})
print('Fields:', json.dumps(field_structure, indent=4))
values = [my_ticket[position] for field_name, position in field_structure.items() if field_name.startswith('departure')]
multiplication = reduce(lambda x, y: x * y, values)
print('Multiplication of all departure* fields:', multiplication)
