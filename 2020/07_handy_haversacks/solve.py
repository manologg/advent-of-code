#!/usr/bin/python
# coding=utf-8
from functools import reduce
import re

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


LINE_REGEX_WITH_PARAMS = r'^(?P<bag>\w+ \w+) bags contain (?P<content>[0-9a-zA-Z ,]+).$'

ZERO_BAGS = r'^no other bags$'
ONE_BAG = r'\d+ \w+ \w+ bags?'
AT_LEAST_ONE_BAG = r'^(' + ONE_BAG + ', )*' + ONE_BAG + '$'

BAG_REGEX_WITH_PARAMS = r'^(?P<amount>\d+) (?P<bag>\w+ \w+) bags?$'


def parse_bag(bag):
    return re.match(BAG_REGEX_WITH_PARAMS, bag).groupdict()


def parse_bags(bags):
    return [parse_bag(x) for x in bags.split(', ')]


def parse_line(line):
    definition = re.match(LINE_REGEX_WITH_PARAMS, line).groupdict()
    bag = definition['bag']
    content = definition['content']

    if re.match(ZERO_BAGS, content):
        return bag, {}
    elif re.match(AT_LEAST_ONE_BAG, content):
        return bag, {x['bag']: int(x['amount']) for x in parse_bags(content)}
    else:
        raise AssertionError('this should not happen!')


def get_possible_bags_containing(definitions, original_bag):
    bags = [x[0] for x in definitions.items() if original_bag in x[1]]
    # print('{} --> {}'.format(original_bag, bags))
    return reduce(set.union, [get_possible_bags_containing(definitions, bag) for bag in bags], set(bags))


def get_all_bags_inside(definitions, original_bag):
    content = definitions[original_bag].items()
    # print('{} --> {}'.format(original_bag, dict(content)))
    return sum([amount * (get_all_bags_inside(definitions, bag) + 1) for bag, amount in content])


line = readline()
definitions = {}
while line:
    bag, content = parse_line(line)
    definitions[bag] = content
    print('{} --> {}'.format(bag, content))

    line = readline()

print('----------------')
possible_bags = get_possible_bags_containing(definitions, 'shiny gold')
print('PART 1 - number of possible bag colors: {}'.format(len(possible_bags)))

print('----------------')
all_bags = get_all_bags_inside(definitions, 'shiny gold')
print('PART 2 - number of possible bag colors: {}'.format(all_bags))
