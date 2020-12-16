#!/usr/bin/python
# coding=utf-8
import copy

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def read_code():
    line = readline()
    code = []
    while line:
        command, offset = line.split(' ')
        code.append({
            'command': command,
            'offset': int(offset)
        })
        line = readline()

    return code


def change_code(code):

    possible_line_changes = [i for i in range(len(code)) if code[i]['command'] in ['nop', 'jmp']]
    print('Possible changes: {}'.format(possible_line_changes))
    print('')

    all_new_programs = []
    for i in possible_line_changes:

        new_code = copy.deepcopy(code)

        if new_code[i]['command'] == 'nop':
            new_code[i]['command'] = 'jmp'
        elif new_code[i]['command'] == 'jmp':
            new_code[i]['command'] = 'nop'
        else:
            raise AssertionError('This should not happen! {}'.format(new_code[i]['command']))

        all_new_programs.append(new_code)

    return all_new_programs


def run(code, pointer, accumulator, already_visited):

    if pointer == len(code):
        print('Program finished!')
        return accumulator

    command = code[pointer]['command']
    offset = code[pointer]['offset']

    if pointer in already_visited:
        raise Exception('This program is endless: {}'.format(already_visited))
    else:
        already_visited.append(pointer)

    if command == 'nop':
        return run(code, pointer + 1, accumulator, already_visited)

    elif command == 'acc':
        return run(code, pointer + 1, accumulator + offset, already_visited)

    elif command == 'jmp':
        return run(code, pointer + offset, accumulator, already_visited)

    else:
        raise AssertionError('Unknown command: {}'.format(command))


code = read_code()
# print(code)
# print('--------------------')

for new_code in change_code(code):

    # print(new_code)

    try:
        accumulator = run(new_code, 0, 0, [])
        print('Accumulator after finishing the program: {}'.format(accumulator))
    except Exception as e:
        # print('This is not the program you are looking for. {}'.format(e))
        pass

    # print('----------')
