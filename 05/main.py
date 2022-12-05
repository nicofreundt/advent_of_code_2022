import copy
import re


def read_stacks():
    with open("input.txt") as file:
        return [[e[1] for e in stack if re.match(r'\S', e)] for stack in zip(*[[line[i:i + 3] for i in range(0, len(line), 4)] for line in file.readlines() if re.match(r'( *\[[A-Z]] *)+', line)][::-1])]


def read_procedures():
    with open("input.txt") as file:
        return [[*map(int, re.findall(r'\d+', line.strip()))] for line in file.readlines() if re.match(r'(move \d+ from \d+ to \d+)', line)]


def crane_9000(procedure_list, stack_list):
    for procedure in procedure_list:
        stack_list[procedure[2] - 1] += [stack_list[procedure[1] - 1].pop() for _ in range(procedure[0])]
    return ''.join([stack[-1] for stack in stack_list])


def crane_9001(procedure_list, stack_list):
    for procedure in procedure_list:
        stack_list[procedure[2] - 1] += [stack_list[procedure[1] - 1].pop() for _ in range(procedure[0])][::-1]
    return ''.join([stack[-1] for stack in stack_list])


if __name__ == "__main__":
    stacks = read_stacks()
    procedures = read_procedures()

    # part one
    print(crane_9000(procedures, copy.deepcopy(stacks)))

    # part two
    print(crane_9001(procedures, copy.deepcopy(stacks)))
