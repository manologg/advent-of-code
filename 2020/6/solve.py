#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()


line = readline()
current_group = None
sum_of_positive_answers = 0
while line:

    line = line[:-1]

    if line:
        positive_answers = [x for x in line]
        if current_group is None:
            current_group = set(positive_answers)
        else:
            current_group.intersection_update(positive_answers)
    else:
        sum_of_positive_answers += len(current_group)
        print('{} --> {}'.format(current_group, len(current_group)))
        current_group = None

    line = readline()

sum_of_positive_answers += len(current_group)
print('{} --> {}'.format(current_group, len(current_group)))

print('Sum of positive answers: {}'.format(sum_of_positive_answers))