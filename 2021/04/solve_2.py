#!/usr/bin/python
# coding=utf-8
import copy
import math
from functools import reduce

input_file = open('input.txt')


def print_card(card):
    for row in card:
        print(' '.join([f'({n})' if marked else f'{n}' for n, marked in row]))


def print_cards(cards):
    for i, card in enumerate(cards):
        print()
        print(f'Card {i}:')
        print_card(card)


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print(f'ignoring line \'{line}\'')


def read_comma_separated_int_line():
    return [int(x) for x in read_line().split(',')]


def read_lines_while_not_empty():
    cards = []
    count = 0
    current_card = []
    line = read_line()
    while line:
        current_card.append([(int(x.strip()), False) for x in line.split(' ') if x])
        count += 1
        if count == 5:
            cards.append(copy.deepcopy(current_card))
            current_card = []
            count = 0
            ignore_line()
        line = read_line()
    return cards


def read_lines():
    numbers = read_comma_separated_int_line()
    ignore_line()
    cards = read_lines_while_not_empty()
    return numbers, cards


def mark(n, cards):
    for card in cards:
        for row in card:
            try:
                i = row.index((n, False))
                row[i] = (n, True)
            except ValueError:
                pass  # it's ok, it's not in the card


def check(cards):
    new_cards = []
    for card in cards:

        keep = True

        for i in range(len(card)):
            row_i = [marked for x, marked in card[i]]
            if all(row_i):
                keep = False

        for i in range(len(card[0])):
            column_i = [card[j][i][1] for j in range(len(card))]
            if all(column_i):
                keep = False

        if keep:
            new_cards.append(card)

    return new_cards


def solve(numbers, cards):
    for n in numbers:
        mark(n, cards)
        print(f'Number: {n}')
        print_cards(cards)
        new_cards = check(cards)
        if len(new_cards) == 0:
            return n, cards[0]
        else:
            cards = new_cards


def sum_unmarked_numbers(card):
    sum = 0
    for row in card:
        for n, marked in row:
            if not marked:
                sum += n
    return sum


def print_solution(number, card):
    unmarked_numbers_sum = sum_unmarked_numbers(card)
    print(f'Solution: {unmarked_numbers_sum} * {number} = {unmarked_numbers_sum * number}')


numbers, cards = read_lines()
print(f'Numbers: {numbers}')
print_cards(cards)

number, card = solve(numbers, cards)
print(f'Last number: {number}')
print_card(card)

print_solution(number, card)
