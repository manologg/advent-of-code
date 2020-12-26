#!/usr/bin/python
# coding=utf-8
import re
from functools import reduce;

input_file = open('input.txt')


def print_title(title):
    print()
    print('{}:'.format(title) if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)


def print_dict(d, title=''):
    print_title(title)
    for key, value in d.items():
        print('{}: {}'.format(key, value))


def parse(line):
    groupdict = re.match(r'^(?P<ingredients>[\w ]+) \(contains (?P<allergens>[\w, ]+)\)$', line).groupdict()
    return {
        'ingredients': groupdict['ingredients'].split(' '),
        'allergens': [x.strip() for x in groupdict['allergens'].split(',')]
    }


def readlines():
    return [parse(line[:-1]) for line in input_file.readlines()]


def find_ingredients(allergen, menu):
    items = [set(item['ingredients']) for item in menu if allergen in item['allergens']]
    return reduce(lambda x, y: x.intersection(y), items)


def find_non_allergens(menu):
    allergens = [x for item in menu for x in item['allergens']]
    return {a: find_ingredients(a, menu) for a in allergens}


def refine(allergens, known_allergens={}):
    if not allergens:
        return known_allergens

    new = {allergen: list(ingredients)[0] for allergen, ingredients in allergens.items() if len(ingredients) == 1}
    for allergen, ingredient in new.items():
        known_allergens[allergen] = ingredient
        del allergens[allergen]

    allergens = {allergen: ingredients - set(new.values()) for allergen, ingredients in allergens.items()}
    return refine(allergens, known_allergens)


menu = readlines()
print_list(menu, 'Menu')

allergens = find_non_allergens(menu)
print_dict(allergens, 'Allergens')

known_allergens = refine(allergens)
print_dict(known_allergens, 'Known allergens')

all_ingredients = [i for item in menu for i in item['ingredients'] if i not in known_allergens.values()]
print()
print('Count of ingredients that cannot possibly contain any of the allergens in the list:', len(all_ingredients))

canonical_list = ','.join([item[1] for item in sorted(known_allergens.items(), key=lambda x: x[0])])
print()
print('Canonical dangerous ingredient list:', canonical_list)
