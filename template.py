#!/usr/bin/env python3
"""This script solves puzzles of https://adventofcode.com/"""

import os
import sys
from aoc_utilities import Input
# import re
# import itertools

# 2 digit day fetched from filename
DAY = os.path.basename(__file__)[3:5]


def solve1(input):
    """Solves part 1."""
    pass


def solve2(input):
    """Solves part2."""
    pass


"""
Use script args to execute the right function.
"""
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '1':
        res = solve1((Input(DAY).readlines()))
        print(res)
    if len(sys.argv) > 1 and sys.argv[1] == '2':
        res = solve2((Input(DAY).readlines()))
        print(res)