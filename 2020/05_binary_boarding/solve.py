#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def translate(string, zero, one):
    return string.replace(zero, '0').replace(one, '1')


def decimal(binary_string):
    return int(binary_string, 2)


def find_missing(what, numbers):
    first = min(numbers)
    last = max(numbers)
    print('{}: [{} - {}]'.format(what, first, last))
    for i in range(first, last + 1):
        if i not in numbers:
            print('{} is missing in {}'.format(i, what))
            return i

    return None


line = readline()
highest_seat_id = 0
all_seats = []
while line:

    row = decimal(translate(line[:7], 'F', 'B'))
    column = decimal(translate(line[7:], 'L', 'R'))
    seat_id = row * 8 + column
    all_seats.append((row, column, seat_id))

    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

    # print('{}: row {}, column {}, seat ID {}.'.format(line, row, column, seat_id))
    line = readline()

print('Highest seat ID: {}'.format(highest_seat_id))

rows = [x[0] for x in all_seats]
columns = [x[1] for x in all_seats]
seat_ids = [x[2] for x in all_seats]

print('missing seat ID: {}'.format(find_missing('seat IDs', seat_ids)))
