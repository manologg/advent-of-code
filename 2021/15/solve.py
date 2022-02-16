#!/usr/bin/python
# coding=utf-8
import itertools
import sys
import cProfile
import io
from pstats import SortKey, Stats

input_file = open('input.txt')


def run_with_profiling(func, *args, **kwargs):
    profile = cProfile.Profile()
    profile.enable()

    # run the code
    try:
        result = func(*args, **kwargs)
    except KeyboardInterrupt:
        pass

    profile.disable()
    stream = io.StringIO()
    sort_by = SortKey.CUMULATIVE
    stats = Stats(profile, stream=stream).sort_stats(sort_by)
    stats.print_stats()
    print(stream.getvalue()[:-2])

    return result


def print_title(title=''):
    print(f'{title}:' if title else '')


def print_list(l, title=''):
    print_title(title)
    for x in l:
        print(x)
    print()


def print_grid(grid, title=''):
    print_title(title)
    for line in grid:
        print(' '.join([str(x) for x in line]))
    print()


def print_simple_list(l, title):
    print(f'{title}: {",".join([str(x) for x in l])}')


def parse(line):
    return [int(x) for x in line]


def read_and_parse_lines():
    return [parse(line[:-1]) for line in input_file.readlines()]


best_risks = dict()
counter = itertools.count()


def solve(grid, i, j, max_i, max_j, level=0, visited=None, current_risk=0):

    global best_risks, max_risk

    if visited is None:
        visited = []
    visited = visited + [(i, j)]

    #print(f'{"-" * level} ({i}, {j}) - [{current_risk}] Visited already: {visited}')

    if i == max_i and j == max_j:
        return 0, [(i, j)]

    # check best risks
    if (i, j) in best_risks:
        return best_risks[(i, j)]

    if current_risk + max_i + max_j - i - j > max_risk:
        return sys.maxsize, None

    risk_down = sys.maxsize
    risk_up = sys.maxsize
    risk_right = sys.maxsize
    risk_left = sys.maxsize

    if i < max_i and (i+1, j) not in visited:
        new_risk = grid[i + 1][j]
        risk_down, path_down = solve(grid, i + 1, j, max_i, max_j, level + 1, visited, current_risk + new_risk)
        risk_down += new_risk

    if j < max_j and (i, j+1) not in visited:
        new_risk = grid[i][j + 1]
        risk_right, path_right = solve(grid, i, j + 1, max_i, max_j, level + 1, visited, current_risk + new_risk)
        risk_right += new_risk

    if i > 0 and (i-1, j) not in visited:
        new_risk = grid[i - 1][j]
        risk_up, path_up = solve(grid, i - 1, j, max_i, max_j, level + 1, visited, current_risk + new_risk)
        risk_up += new_risk

    if j > 0 and (i, j-1) not in visited:
        new_risk = grid[i][j - 1]
        risk_left, path_left = solve(grid, i, j - 1, max_i, max_j, level + 1, visited, current_risk + new_risk)
        risk_left += new_risk

    min_risk = min([risk_down, risk_up, risk_right, risk_left])

    if min_risk == sys.maxsize:
        return sys.maxsize, None

    if risk_down == min_risk:
        path = path_down
    elif risk_up == min_risk:
        path = path_up
    elif risk_right == min_risk:
        path = path_right
    elif risk_left == min_risk:
        path = path_left

    path = [(i, j)] + path
    #print('             ')
    #print(f'Min risk for ({i}, {j}): {min_risk} - {path}')
    #print('             ')

    best_risks[(i, j)] = (min_risk, path)

    return min_risk, path


def calculate_down_right_risk(grid, start_i, start_j):
    return sum([grid[i][0] for i in range(start_i + 1, len(grid))]) \
           + sum(grid[len(grid) - 1][start_j + 1:])


grid = read_and_parse_lines()
max_i = len(grid) - 1
max_j = len(grid[0]) - 1
max_risk = 467  # calculate_down_right_risk(grid, 0, 0)
best_risk = run_with_profiling(solve, *[grid, 0, 0, max_i, max_j])

# for key, value in best_risks.items():
#     print(f'{key} - {value}')
print(f'Lowest total risk: {best_risk}')
