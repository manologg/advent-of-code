#!/usr/bin/python
# coding=utf-8

from copy import deepcopy


input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def run(program, i):
    command = program[i]

    if command == 99:
        return

    first = program[program[i + 1]]
    second = program[program[i + 2]]
    result_i = program[i + 3]

    if command == 1:
        program[result_i] = first + second
    if command == 2:
        program[result_i] = first * second

    run(program, i + 4)


program = [int(x) for x in readline().split(',')]
for noun in range(100):
    for verb in range(100):
        new_program = deepcopy(program)
        new_program[1] = noun
        new_program[2] = verb
        run(new_program, 0)
        if new_program[0] == 19690720:
            print(100 * noun + verb)

