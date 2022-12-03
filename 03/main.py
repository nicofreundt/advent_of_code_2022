def rucksacks():
    with open("input.txt") as file:
        return [[sack[:len(sack)//2], sack[len(sack)//2:].strip()] for sack in file.readlines()]


def calc_priority_sum(sacks):
    order = "".join([chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)])
    duplicates = [sum(order.index(item)+1 for item in set(sack[0]) if item in sack[1]) for sack in sacks]
    return sum(duplicates)


def calc_priority_sum_group(sacks):
    order = "".join([chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)])
    groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    duplicates = [sum(order.index(item)+1 for item in set(''.join(group[0])) if item in ''.join(group[1]) and item in ''.join(group[2])) for group in groups]
    return sum(duplicates)


if __name__ == "__main__":
    # part one
    print(calc_priority_sum(rucksacks()))

    # part two
    print(calc_priority_sum_group(rucksacks()))
