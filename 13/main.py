"""Advent of Code Day 13"""
import ast
import copy
from functools import cmp_to_key
import math


def read_input() -> list:
    '''read input file and return interpreted lines as list'''
    with open("input.txt", encoding="utf-8") as file:
        return [ast.literal_eval(line.strip()) for line in file if line.strip() != '']


def compare(value_a, value_b):
    '''compare first and second value'''
    a_copy = copy.deepcopy(value_a)
    b_copy = copy.deepcopy(value_b)
    if all(isinstance(value, list) for value in [a_copy, b_copy]):
        value = 0
        while len(a_copy) and len(b_copy) and not abs(value):
            value = compare(a_copy.pop(0), b_copy.pop(0))
        return value if abs(value) else compare(len(a_copy), len(b_copy))
    if all(isinstance(value, int) for value in [a_copy, b_copy]):
        return 1 if a_copy > b_copy else (a_copy == b_copy) - 1
    if isinstance(a_copy, list):
        return compare(a_copy, [b_copy])
    return compare([a_copy], b_copy)


if __name__ == "__main__":
    data = read_input()

    # part one
    arr = [[data[i], data[i+1]] for i in range(0, len(data), 2)]
    print(sum(value * (x + 1) for x, value in enumerate([compare(a, b) == -1 for a, b in arr])))

    # part two
    sorted_new_data = sorted(data + [[[2]], [[6]]], key=cmp_to_key(compare))
    print(math.prod(x + 1 for x, value in enumerate(sorted_new_data) if value in [[[2]], [[6]]]))
