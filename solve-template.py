#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


x = readline().split(',')
for i in x:
    pass

print(x)
