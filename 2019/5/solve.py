#!/usr/bin/python
# coding=utf-8


input_file = open('input.txt')
INPUT = 5

# COMMAND TYPES
WRITE = 'WRITE'
OUTPUT = 'OUTPUT'
JUMP = 'JUMP'


def sum(program, p1, p2, res_i):
    program[res_i] = p1 + p2


def multiplication(program, p1, p2, res_i):
    program[res_i] = p1 * p2


def input(program, res_i):
    program[res_i] = INPUT


def output(p1):
    print(p1)


def jump_if_true(p1, p2):
    return p2 if p1 else None


def jump_if_false(p1, p2):
    return p2 if not p1 else None


def less_than(program, p1, p2, res_i):
    program[res_i] = 1 if p1 < p2 else 0


def equals(program, p1, p2, res_i):
    program[res_i] = 1 if p1 == p2 else 0


COMMANDS = {
    1: {
        'type': WRITE,
        'num_of_params': 2,
        'function': sum,
    },
    2: {
        'type': WRITE,
        'num_of_params': 2,
        'function': multiplication,
    },
    3: {
        'type': WRITE,
        'num_of_params': 0,
        'function': input,
    },
    4: {
        'type': OUTPUT,
        'num_of_params': 1,
        'function': output,
    },
    5: {
        'type': JUMP,
        'num_of_params': 2,
        'function': jump_if_true,
    },
    6: {
        'type': JUMP,
        'num_of_params': 2,
        'function': jump_if_false,
    },
    7: {
        'type': WRITE,
        'num_of_params': 2,
        'function': less_than,
    },
    8: {
        'type': WRITE,
        'num_of_params': 2,
        'function': equals,
    },
}


def readline():
    return input_file.readline()[:-1]


def get_param_mode(command, i):
    return command // (10 ** (i + 1)) % 10


def get_param(program, i, mode):
    # print('get param i={} and mode={}'.format(i, mode))

    if mode == 0:  # position
        return program[program[i]]

    elif mode == 1:  # immediate
        return program[i]

    else:
        raise SyntaxError('mode must be 0 or 1')


def run(program, pointer):
    command = program[pointer]
    opcode = command % 100

    # print('command: {}'.format(command))
    # print('opcode: {}'.format(opcode))

    if opcode == 99:
        print('HALT!')
        return

    elif opcode in range(1, 9):

        type = COMMANDS[opcode]['type']
        num_of_params = COMMANDS[opcode]['num_of_params']
        function = COMMANDS[opcode]['function']

        params = []
        for i in range(1, num_of_params + 1):
            mode = get_param_mode(command, i)
            param = get_param(program, pointer + i, mode)
            params.append(param)

        if type == WRITE:
            res_i = program[pointer + num_of_params + 1]
            function(program, *params, res_i)
            run(program, pointer + num_of_params + 2)

        elif type == OUTPUT:
            function(*params)
            run(program, pointer + num_of_params + 1)

        elif type == JUMP:
            new_pointer = function(*params)
            run(program, new_pointer if new_pointer is not None else pointer + num_of_params + 1)

        else:
            raise SyntaxError('result_type must be \'INDEX\' or None')

    else:
        raise SyntaxError('opcode must be 1, 2, 3, 4 or 99')


program = [int(x) for x in readline().split(',')]
run(program, 0)
