#!/usr/bin/python
# coding=utf-8
import re

input_file = open('input.txt')


def readline():
    return input_file.readline()


def is_valid(passport):

    print('\nChecking passport: {}'.format(passport))

    try:

        byr = passport['byr']
        int_byr = int(byr)
        if not re.match('^\d{4}$', byr) or int_byr < 1920 or int_byr > 2002:
            print('field \'byr\' does not comply with specification')
            return False

        iyr = passport['iyr']
        int_iyr = int(iyr)
        if not re.match('^\d{4}$', iyr) or int_iyr < 2010 or int_iyr > 2020:
            print('field \'iyr\' does not comply with specification')
            return False

        eyr = passport['eyr']
        int_eyr = int(eyr)
        if not re.match('^\d{4}$', eyr) or int_eyr < 2020 or int_eyr > 2030:
            print('field \'eyr\' does not comply with specification')
            return False

        hgt = passport['hgt']
        match = re.match(r'^(?P<value>\d+)(?P<unit>(cm|in))$', hgt)
        if not match:
            print('field \'hgt\' does not comply with specification')
            return False
        else:
            value = int(match.groupdict()['value'])
            unit = match.groupdict()['unit']
            if unit == 'cm' and (value < 150 or value > 193):
                print('field \'hgt\' (cm) does not comply with specification')
                return False
            if unit == 'in' and (value < 59 or value > 76):
                print('field \'hgt\' (in) does not comply with specification')
                return False

        hcl = passport['hcl']
        if not re.match('^#[0-9a-f]{6}$', hcl):
            print('field \'hcl\' does not comply with specification')
            return False

        ecl = passport['ecl']
        if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl):
            print('field \'ecl\' does not comply with specification')
            return False

        pid = passport['pid']
        if not re.match('^\d{9}$', pid):
            print('field \'pid\' does not comply with specification')
            return False

    except KeyError as e:
        print('NOT VALID')
        return False

    print('valid!')
    return True


line = readline()
current_passport = {}
valid_passports = 0
while line:

    line = line[:-1]

    if line:
        for field in line.split(' '):
            match = re.match(r'(?P<key>\w+):(?P<value>#?\w+)', field)
            current_passport.update({match.groupdict()['key']: match.groupdict()['value']})
    else:
        if is_valid(current_passport):
            valid_passports += 1
        current_passport = {}

    line = readline()

if is_valid(current_passport):
    valid_passports += 1

print('Valid passwords: {}'.format(valid_passports))
