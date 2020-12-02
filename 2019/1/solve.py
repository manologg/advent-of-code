#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def calculate_fuel(mass):
    fuel = int(mass / 3) - 2
    if fuel > 0:
        return fuel + calculate_fuel(fuel)
    else:
        return 0


total = 0
line = readline()
while line:
    mass = int(line)
    total += calculate_fuel(mass)
    line = readline()

print(total)
