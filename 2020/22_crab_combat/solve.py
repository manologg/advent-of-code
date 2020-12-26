#!/usr/bin/python
# coding=utf-8
from copy import deepcopy

input_file = open('input.txt')


def read_line():
    return input_file.readline()[:-1]


def ignore_line():
    line = read_line()
    print('ignoring line \'{}\''.format(line))


def read_lines_while_not_empty():
    line = read_line()
    x = []
    while line:
        x.append(int(line))
        line = read_line()
    return x


def move_cards(winner, first, second):
    winner.extend([first, second])


def play_round(x, y, x_already_played, y_already_played, round, subgame):

    # print(f'Player 1\'s deck: {x}')
    # print(f'Player 2\'s deck: {y}')

    if x in x_already_played or y in y_already_played:
        return 'x', x

    x0 = x.pop(0)
    y0 = y.pop(0)
    # print(f'Player 1 plays: {x0}')
    # print(f'Player 2 plays: {y0}')

    if len(x) >= x0 and len(y) >= y0:
        winner, _ = play(deepcopy(x[:x0]), deepcopy(y[:y0]), [], [], subgame + 1)
        # print(f'...anyway, back to game {subgame}.')
    else:
        winner = 'x' if x0 > y0 else 'y'

    x_already_played.append([x0] + deepcopy(x))
    y_already_played.append([y0] + deepcopy(y))

    if winner == 'x':
        # print(f'Player 1 wins round {round} of game {subgame}!')
        move_cards(x, x0, y0)
    else:
        # print(f'Player 2 wins round {round} of game {subgame}!')
        move_cards(y, y0, x0)
    # print()

    return '', None


def play(x, y, x_already_played=[], y_already_played=[], subgame=1):

    round = 1
    # print(f'=== Game {subgame} ===')
    while x and y:
        # print(f'-- Round {round} (Game {subgame}) --')
        name, winner = play_round(x, y, x_already_played, y_already_played, round, subgame)
        if winner:
            return name, winner
        if round % 1000 == 0:
            print('|{} [{}]: {} - {}'.format('\t' * subgame, round, len(x), len(y)))
        round += 1
    if x:
        # print(f'The winner of game {subgame} is player 1!')
        return 'x', x
    else:
        # print(f'The winner of game {subgame} is player 2!')
        return 'y', y


def calculate_score(winner):
    score = 0
    for i, x in enumerate(winner[::-1], start=1):
        score += i * x
    return score


ignore_line()
x = read_lines_while_not_empty()
ignore_line()
y = read_lines_while_not_empty()
print('Player 1: {} (len={})'.format(x, len(x)))
print('Player 2: {} (len={})'.format(y, len(y)))

name, winner = play(x, y)
print('Winner - player {}: {} (len={})'.format('1' if winner == 'x' else '2', winner, len(winner)))
score = calculate_score(winner)
print('Score:', score)
