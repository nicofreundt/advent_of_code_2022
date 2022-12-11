"""Advent of Code Day 11"""
import copy
import math
import re


class Monkey:
    '''Monkey in the Middle - Participant'''

    def __init__(self, index) -> None:
        self.index = index
        self.items = []
        self.operation = None
        self.test = None
        self.monkeys = []
        self.inspections = 0

    # def __repr__(self) -> str:
    #    '''start representation of monkey'''
    #    return f'Monkey {self.index}:\n  Starting items: {", ".join(str(item) for item in self.items)}\n  Operation: {self.operation}\n  Test: divisible by {self.test}\n    If true: throw to monkey {self.monkeys[0]}\n    If false: throw to monkey {self.monkeys[1]}\n\n'

    def __repr__(self) -> str:
        return f'Monkey {self.index} inspected {self.inspections} items.'

    def __calc_operation(self) -> int:
        '''calculate the given operation'''
        parts = self.operation.split()
        first = int(parts[0]) if parts[0] != 'old' else self.items[0]
        operator = parts[1]
        second = int(parts[2]) if parts[2] != 'old' else self.items[0]
        return first + second if operator == "+" else first * second

    def inspect_item_efficient(self, monkeys):
        '''inspect specific item efficient'''
        mod = math.prod(monkey.test for monkey in monkeys)
        cur_worrieness = self.__calc_operation() % mod
        monkeys[self.monkeys[cur_worrieness % self.test != 0]].items.append(cur_worrieness)
        self.inspections += 1
        self.items.pop(0)

    def inspect_item_normal(self, monkeys):
        '''inspect specific item normal'''
        cur_worrieness = self.__calc_operation() // 3
        monkeys[self.monkeys[cur_worrieness % self.test != 0]].items.append(cur_worrieness)
        self.inspections += 1
        self.items.pop(0)


def read_monkeys() -> list[Monkey]:
    '''read monkeys from file'''
    with open("input.txt", encoding="utf-8") as file:
        monkeys = []

        for index, line in enumerate(file.readlines()):
            if index % 7 == 0:
                monkeys.append(Monkey(int(re.search(r"\d+", line).group())))
            elif index % 7 == 1:
                monkeys[index // 7].items = [int(item) for item in re.findall(r"\d+", line)]
            elif index % 7 == 2:
                monkeys[index // 7].operation = line.strip().split(' = ')[-1]
            elif index % 7 == 3:
                monkeys[index // 7].test = int(re.search(r"\d+", line).group())
            elif index % 7 == 4:
                monkeys[index // 7].monkeys.append(int(re.search(r"\d+", line).group()))
            elif index % 7 == 5:
                monkeys[index // 7].monkeys.append(int(re.search(r"\d+", line).group()))

        return monkeys


if __name__ == "__main__":
    monkey_participants = read_monkeys()

    # part one
    ROUNDS = 20
    first_monkeys = copy.deepcopy(monkey_participants)

    for _ in range(ROUNDS):
        for monkey in first_monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspect_item_normal(first_monkeys)

    print(*first_monkeys, sep="\n")
    print(math.prod(monkey.inspections for monkey in sorted(first_monkeys, key=lambda x: x.inspections)[-2:]), end="\n\n")

    # part two
    ROUNDS = 10000
    second_monkeys = copy.deepcopy(monkey_participants)

    for _ in range(ROUNDS):
        for monkey in second_monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspect_item_efficient(second_monkeys)

    print(*second_monkeys, sep="\n")
    print(math.prod(monkey.inspections for monkey in sorted(second_monkeys, key=lambda x: x.inspections)[-2:]))
