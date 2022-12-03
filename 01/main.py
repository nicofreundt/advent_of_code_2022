def calories_list():
    with open('input.txt') as file:
        cals = [cal for cal in file.readlines()]
        return cals


def elfes(list_of_calories):
    return [sum(int(cal) for cal in cals.split("\n")) for cals in "".join(list_of_calories).split("\n\n")]


def most_calories(cals_per_elf):
    return max(cals_per_elf)


def most_three_calories(cals_per_elf):
    sorted_elfes = sorted(cals_per_elf)
    return sum(sorted_elfes[::-1][:3])


if __name__ == "__main__":
    calories = calories_list()
    calories_per_elf = elfes(calories)

    # part one
    print(most_calories(calories))

    # part two
    print(most_three_calories(calories))
