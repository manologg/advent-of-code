#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


################################################################

def readline():
    return input_file.readline()[:-1]


def ignore_line():
    line = readline()
    print('ignoring line \'{}\'', line)


line = readline()
x = []
while line:
    x.append(line)
    line = readline()


################################################################


def readlines():
    return [int(x[:-1]) for x in input_file.readlines()]


x = readlines()

################################################################

print(x)
