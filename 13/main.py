"""Advent of Code Day 13"""
import ast
from functools import cmp_to_key
import math


def read_input() -> list:
    '''read input file and return interpreted lines as list'''
    with open("input.txt", encoding="utf-8") as file:
        return [ast.literal_eval(line.strip()) for line in file if line.strip() != '']


def compare(val_a, val_b):
    '''compare first and second value'''
    if all(isinstance(value, list) for value in [val_a, val_b]):
        return comps[0] if len(comps:=[comp for i in range(min(len(val_a), len(val_b))) if abs(comp:=compare(val_a[i], val_b[i]))]) > 0 else compare(len(val_a), len(val_b))
    if all(isinstance(value, int) for value in [val_a, val_b]):
        return 1 if val_a > val_b else (val_a == val_b) - 1
    if isinstance(val_a, list):
        return compare(val_a, [val_b])
    return compare([val_a], val_b)


if __name__ == "__main__":
    data = read_input()

    # part one
    arr = [[data[i], data[i+1]] for i in range(0, len(data), 2)]
    print(sum(value * (x + 1) for x, value in enumerate([compare(a, b) == -1 for a, b in arr])))

    # part two
    sorted_new_data = sorted(data + [[[2]], [[6]]], key=cmp_to_key(compare))
    print(math.prod(x + 1 for x, value in enumerate(sorted_new_data) if value in [[[2]], [[6]]]))
