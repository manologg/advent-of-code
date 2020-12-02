#!/usr/bin/python
# coding=utf-8

input_file = open('input.txt')


def readline():
    return input_file.readline()[:-1]


def read_all_nums():
    line = readline()
    nums = []
    while line:
        nums.append(int(line))
        line = readline()
    return nums


def find(nums):
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == 2020:
                    print("Found! {} + {} + {} = 2020. If you multiply them together: {}".format(i, j, k, i * j * k))
                    return


nums = read_all_nums()
print(nums)
find(nums)
