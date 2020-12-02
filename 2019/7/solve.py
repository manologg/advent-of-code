#!/usr/bin/python
# coding=utf-8
from copy import deepcopy
from functools import reduce
from itertools import permutations

input_file = open('input.txt')

# COMMAND TYPES
WRITE = 'WRITE'
INPUT = 'INPUT'
OUTPUT = 'OUTPUT'
JUMP = 'JUMP'


def sum(code, p1, p2, res_i):
    code[res_i] = p1 + p2


def multiplication(code, p1, p2, res_i):
    code[res_i] = p1 * p2


def read_input(code, input, res_i):
    code[res_i] = input.pop(0)
    # print('read {} from input'.format(code[res_i]))


def write_output(output, p1):
    output.append(p1)
    # print('wrote {} to output'.format(p1))


def jump_if_true(p1, p2):
    return p2 if p1 else None


def jump_if_false(p1, p2):
    return p2 if not p1 else None


def less_than(code, p1, p2, res_i):
    code[res_i] = 1 if p1 < p2 else 0


def equals(code, p1, p2, res_i):
    code[res_i] = 1 if p1 == p2 else 0


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
        'type': INPUT,
        'num_of_params': 0,
        'function': read_input,
    },
    4: {
        'type': OUTPUT,
        'num_of_params': 1,
        'function': write_output,
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


def get_param(code, i, mode):

    if mode == 0:  # position
        return code[code[i]]

    elif mode == 1:  # immediate
        return code[i]

    else:
        raise SyntaxError('mode must be 0 or 1')


def run(program):
    """
    Runs the given program
    :param program:
    :return: True if the program finished or False if the program is waiting for input
    """

    code = program['code']
    pointer = program['pointer']
    input = program['input']
    output = program['output']

    command = code[pointer]
    opcode = command % 100

    if opcode == 99:
        # print('HALT!')
        program['halt'] = True
        return

    elif opcode in range(1, 9):

        type = COMMANDS[opcode]['type']
        num_of_params = COMMANDS[opcode]['num_of_params']
        function = COMMANDS[opcode]['function']

        params = []
        for i in range(1, num_of_params + 1):
            mode = get_param_mode(command, i)
            param = get_param(code, pointer + i, mode)
            params.append(param)

        if type == WRITE:
            res_i = code[pointer + num_of_params + 1]
            function(code, *params, res_i)
            program['pointer'] = pointer + num_of_params + 2
            run(program)

        elif type == INPUT:
            # print('I need to read something')
            if not input:
                program['halt'] = False
                return

            res_i = code[pointer + num_of_params + 1]
            function(code, input, res_i)
            program['pointer'] = pointer + num_of_params + 2
            run(program)

        elif type == OUTPUT:
            function(output, *params)
            program['pointer'] = pointer + num_of_params + 1
            run(program)

        elif type == JUMP:
            new_pointer = function(*params)
            program['pointer'] = new_pointer if new_pointer is not None else pointer + num_of_params + 1
            run(program)

        else:
            raise SyntaxError('result_type must be \'INDEX\' or None')

    else:
        raise SyntaxError('opcode must be 1-8 or 99')


def all_programs_stopped(programs):
    return reduce((lambda x, y: x and y), [p['halt'] for p in programs])


def run_with_settings(original_program, settings):

    programs = [{
                    'code': deepcopy(original_program),
                    'input': [s],
                    'output': [],
                    'pointer': 0,
                    'halt': False,
                } for s in settings]

    last_output = [0]
    program_to_run = 0
    while not all_programs_stopped(programs):
        program = programs[program_to_run]

        program['input'].extend(last_output)
        program['output'] = []
        # print('Starting program {} with input: {}'.format(program_to_run, program['input']))

        run(program)
        # print('Program {} halted: {}'.format(program_to_run, program['halt']))

        # print('output to be used in the next iteration: {}'.format(program['output']))
        last_output = program['output']
        program_to_run = program_to_run + 1 if program_to_run < 4 else 0
        # print()

    return programs[-1]['output'][-1]

program = [int(x) for x in readline().split(',')]
highest = 0
for permutation in permutations(range(5, 10), 5):
    program_copy = deepcopy(program)
    # print('-- Running {} --'.format(permutation))
    output = run_with_settings(program_copy, permutation)
    if output > highest:
        highest = output
    # print('-----------------------------')

print('Highest output: {}'.format(highest))