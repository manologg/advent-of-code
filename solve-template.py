#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def readlines():
    return [x[:-1] for x in input_file.readlines()]


line = readline()
x = []
while line:
    x.append(line)
    line = readline()

print(x)
