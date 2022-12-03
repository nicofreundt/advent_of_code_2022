def strategy():
    with open("input.txt") as file:
        rounds = [r.split() for r in file.readlines()]
        return rounds


def calc_score():
    score_board = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    score = 0
    for r in strategy():
        if r[0] == 'ABC'['XYZ'.index(r[1])]:
            score += 3
        if r[0] == 'A' and r[1] == 'Y' or r[0] == 'B' and r[1] == 'Z' or r[0] == 'C' and r[1] == 'X':
            score += 6
        score += score_board.get(r[1])
    return score


def my_choice(opponent, outcome):
    if outcome == 'Y':
        return 'XYZ'['ABC'.index(opponent)]
    elif outcome == 'Z':
        if opponent == 'A':
            return 'Y'
        elif opponent == 'B':
            return 'Z'
        else:
            return 'X'
    else:
        if opponent == 'A':
            return 'Z'
        elif opponent == 'B':
            return 'X'
        else:
            return 'Y'


def calc_score_by_outcome():
    score_board = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    score = 0
    for r in strategy():
        if r[1] == 'Y':
            score += 3
        if r[1] == 'Z':
            score += 6
        score += score_board.get(my_choice(r[0], r[1]))
    return score


if __name__ == "__main__":
    # part one
    print(calc_score())

    # part two
    print(calc_score_by_outcome())
