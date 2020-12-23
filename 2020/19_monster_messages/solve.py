#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def ignore_line():
    line = readline()
    print('ignoring line \'{}\'', line)


def read_rules():
    line = readline()
    rules = {}
    while line:
        number, rule = line.split(':')
        rules[number] = rule.strip()
        line = readline()
    return rules


def read_words():
    return [x[:-1] for x in input_file.readlines()]


def print_all(rules, words):
    print('rules:')
    for number, rule in rules.items():
        print('{}: {}'.format(number, rule))
    print('words:', words)


def translate(rules, position='0'):
    rule = rules[position]
    match = re.match(r'^"(?P<char>\w)"$', rule)
    if match:
        rules[position] = match.groupdict().get('char')
    elif re.match(r'.*\d.*', rule):
        translation = ''
        for x in rule.split(' '):
            if x in ['|', '(', ')', '+', '*']:
                translation += x
            else:
                translate(rules, position=x)
                translation += rules[x]

        rules[position] = '(' + translation + ')'


rules = read_rules()
words = read_words()
print_all(rules, words)

# Original rule 8: 42 | 42 8
rules['8'] = '( 42 ) +'

# Original rule 11: 42 31 | 42 11 31
# yes, this is a little bit of a hack
rules['11'] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31'

translate(rules)

rule = rules['0']
valid_words = [w for w in words if re.match('^' + rule + '$', w)]
print_all(rules, valid_words)
print('Messages matching rule 0:', len(valid_words))

print('rule  0:', rules['0'])
print('rule  8:', rules['8'])
print('rule 11:', rules['11'])
