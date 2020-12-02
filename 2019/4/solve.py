#!/usr/bin/python
# coding=utf-8

MIN = 136818
MAX = 685979


def is_never_descending(n):
    s = str(n)
    last = s[0]
    for c in s[1:]:
        if c < last:
            return False
        last = c
    return True


def has_the_same_2_consecutive_digits(n):
    s = str(n)
    last = s[0]
    same_count = 1
    groups = []
    for c in s[1:]:
        if c != last:
            groups.append(same_count)
            same_count = 1
        else:
            same_count += 1
        last = c
    groups.append(same_count)
    return 2 in groups


solutions = 0
for i in range(MIN, MAX):
    if is_never_descending(i) and has_the_same_2_consecutive_digits(i):
        solutions += 1

print(solutions)
