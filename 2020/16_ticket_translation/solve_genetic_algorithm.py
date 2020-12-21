#!/usr/bin/python
# coding=utf-8
import re
from copy import deepcopy
from functools import reduce
from itertools import count
from random import sample, randrange

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


def find_position(field_name, valid_values, tickets, taken):
    for i in range(len(tickets[0])):
        if i in taken:
            continue
        valid_position = check_all_tickets(tickets, i, valid_values)
        if valid_position:
            return i
    raise Exception('No valid positions for field \'{}\' (got {} fields until here)'.format(field_name, len(taken)),
                    len(taken))


def find_structure(fields, order, tickets):
    field_structure = {}
    taken = []
    for field_name in order:
        position = find_position(field_name, fields[field_name], tickets, taken)
        taken.append(position)
        field_structure[field_name] = position

    print('Fields found! // Field structure: {}'.format(field_structure))
    return field_structure


POPULATION_SIZE = 30
DEAD_POPULATION = 15
OFFSPRING = POPULATION_SIZE - DEAD_POPULATION
MUTATIONS = 15
GOAL = 20


def initialize(fields):
    field_names = [x for x in fields.keys()]
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(sample(field_names, len(field_names)))
    return population


def evaluate(population, fields, valid_tickets):
    scores = []
    for individual in population:
        try:
            _ = find_structure(fields, individual, valid_tickets)
            scores.append((individual, 20))
        except Exception as e:
            score = e.args[1]
            scores.append((individual, score))
    return scores


def selection(scores):
    sorted_scores = sorted(scores, key=lambda x: -x[1])
    return [x[0] for x in sorted_scores[:DEAD_POPULATION]]


def get_2_random_numbers(stop):
    x = y = 0
    while x == y:
        x = randrange(stop)
        y = randrange(stop)
    return x, y


def crossover(population):
    new_population = []
    for _ in range(OFFSPRING):
        i, j = get_2_random_numbers(len(population))
        dominant = deepcopy(population[i])
        recessive = deepcopy(population[j])
        first_possitions = randrange(5)
        first_dominant = dominant[:first_possitions]
        for x in first_dominant:
            recessive.remove(x)
        new_individual = first_dominant + recessive
        new_population.append(new_individual)

    return new_population


def mutation(population):
    new_population = []
    for old_individual in population:
        new_individual = deepcopy(old_individual)
        for _ in range(MUTATIONS):
            i, j = get_2_random_numbers(len(new_individual))
            temp = new_individual[i]
            new_individual[i] = new_individual[j]
            new_individual[j] = temp
        new_population.append(new_individual)
    return new_population


def try_to_find_structure_with_genetic_algorithm(fields, valid_tickets):
    print('POPULATION_SIZE:', POPULATION_SIZE)
    print('DEAD_POPULATION:', DEAD_POPULATION)
    print('MUTATIONS:', MUTATIONS)

    population = initialize(fields)
    for generation in count(start=0, step=1):
        scores = evaluate(population, fields, valid_tickets)
        only_scores = sorted([x[1] for x in scores], reverse=True)
        max_score = max(only_scores)
        print('Generation: {} // Max. score: {}'.format(generation, max_score))
        print('First field:', ''.join([x[0][0][0] for x in scores]))
        print('Scores:', only_scores)
        print()
        if max_score == GOAL:
            print('Found {}!'.format(GOAL))
            order = [x[0] for x in scores if x[1] == GOAL][0]
            return find_structure(fields, order, valid_tickets)

        population = selection(scores)
        new_population = crossover(population)
        new_population = mutation(new_population)
        population.extend(new_population)


fields, my_ticket, valid_tickets = read_input()
field_structure = try_to_find_structure_with_genetic_algorithm(fields, valid_tickets)
values = [my_ticket[position] for field_name, position in field_structure.items() if field_name.startswith('departure')]
multiplication = reduce(lambda x, y: x * y, values)
print('Multiplication of all departure* fields:', multiplication)
