#!/usr/bin/env python3
"""This script solves puzzles of https://adventofcode.com/"""

import os
import sys

from aoc_utilities import Input, test_input
from itertools import product
from operator import itemgetter

# 2 digit day fetched from filename
DAY = os.path.basename(__file__)[3:5]


def neighbors_26(point):
    """returns a set of (x,y,z) positions for the 26 positions around point """
    x = [point[0] - 1, point[0], point[0] + 1]
    y = [point[1] - 1, point[1], point[1] + 1]
    z = [point[2] - 1, point[2], point[2] + 1]
    return set(product(x, y, z)) - set([point])


def parser(data):
    """returns a list of list of coordinates (tuples) of acitvated cubes"""
    activated_cubes = []
    z = 0
    for y, line in enumerate(data):
        for x, value in enumerate(line.strip()):
            if value == "#":
                activated_cubes.append((x, y, z))
    return activated_cubes


def get_bounds(grid):
    """returns min and max index used in each dimention"""
    xlist = [t[0] for t in grid]
    ylist = [t[1] for t in grid]
    zlist = [t[2] for t in grid]
    return ((min(xlist), max(xlist)), (min(ylist), max(ylist)), (min(zlist),
                                                                 max(zlist)))


def cycle(grid):
    """returns the grid resulting of a cycle on the input grid"""

    bounds = get_bounds(grid)
    new_grid = []

    for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
        for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
            for z in range(bounds[2][0] - 1, bounds[2][1] + 2):
                neighbors = neighbors_26((x, y, z))
                active_neighbors = []
                for n in neighbors:
                    if n in grid:
                        active_neighbors.append(n)
                if (x, y, z) in grid and 2 <= len(active_neighbors) <= 3:
                    #                    print(
                    #                        f'({x}, {y}, {z}) remains active thanks to {active_neighbors}'
                    #                    )
                    new_grid.append((x, y, z))
                if (x, y, z) not in grid and len(active_neighbors) == 3:
                    #                    print(
                    #                        f'({x}, {y}, {z}) becomes active thanks to {active_neighbors}'
                    #                    )
                    new_grid.append((x, y, z))
    return new_grid


def gprint(grid, z):
    """pretty print of the grid"""
    bounds = get_bounds(grid)
    # print(f'grid for z = {z}')
    for y in range(bounds[1][0], bounds[1][1] + 1):
        line = []
        for x in range(bounds[0][0], bounds[0][1] + 1):
            if (x, y, z) in grid:
                line.append("#")
            else:
                line.append(".")
        print(''.join(line))
    return


def solve1(data):
    """Solves part 1."""
    nb_cycle = 6
    grid = parser(data)
    for _ in range(nb_cycle):
        grid = cycle(grid)

    # print(grid)
    # bounds = get_bounds(grid)
    # for z in range(bounds[2][0], bounds[2][1] + 1):
    #     gprint(grid, z)
    #     print()

    return len(grid)


#
#
#
#
#


def neighbors_80(point):
    """returns a set of (x,y,z) positions for the 26 positions around point """
    x = [point[0] - 1, point[0], point[0] + 1]
    y = [point[1] - 1, point[1], point[1] + 1]
    z = [point[2] - 1, point[2], point[2] + 1]
    w = [point[3] - 1, point[3], point[3] + 1]
    return set(product(x, y, z, w)) - set([point])


def parser2(data):
    """returns a list of list of coordinates (tuples) of acitvated cubes"""
    active_cubes = set()
    for y, line in enumerate(data):
        for x, value in enumerate(line.strip()):
            if value == "#":
                active_cubes.add((x, y, 0, 0))
    return active_cubes


def get_bounds2(grid):
    """returns min and max index used in each dimention"""
    ndims = len(next(iter(grid)))
    bounds = []

    for i in range(ndims):
        lo = min(map(itemgetter(i), grid))
        hi = max(map(itemgetter(i), grid))
        bounds.append((lo, hi))
    return bounds


def cycle2(grid):
    """returns the grid resulting of a cycle on the input grid"""

    bounds = get_bounds2(grid)
    new_grid = set()

    for x in range(bounds[0][0] - 1, bounds[0][1] + 2):
        for y in range(bounds[1][0] - 1, bounds[1][1] + 2):
            for z in range(bounds[2][0] - 1, bounds[2][1] + 2):
                for w in range(bounds[3][0] - 1, bounds[3][1] + 2):
                    cube = (x, y, z, w)
                    neighbors = neighbors_80(cube)
                    active_neighbors = []
                    for n in neighbors:
                        if n in grid:
                            active_neighbors.append(n)
                    if cube in grid and 2 <= len(active_neighbors) <= 3:
                        new_grid.add(cube)
                    if cube not in grid and len(active_neighbors) == 3:
                        new_grid.add(cube)
    return new_grid


def solve2(data):
    """Solves part2."""
    nb_cycle = 6
    grid = parser2(data)
    for _ in range(nb_cycle):
        grid = cycle2(grid)
    return len(grid)


"""
Use script args to execute the right function.
"""
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '1':
        res = solve1((Input(DAY).readlines()))
        print(res)
    if len(sys.argv) > 1 and sys.argv[1] == '1t':
        res = solve1((test_input(DAY).readlines()))
        print(res)
    if len(sys.argv) > 1 and sys.argv[1] == '2':
        res = solve2((Input(DAY).readlines()))
        print(res)
    if len(sys.argv) > 1 and sys.argv[1] == '2t':
        res = solve2((test_input(DAY).readlines()))
        print(res)
