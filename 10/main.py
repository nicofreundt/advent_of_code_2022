def yield_signal_strengths(actions):
    '''return the right signal strengths'''
    rounds = [20, 60, 100, 140, 180, 220]
    cur_round = 1
    signal = 1
    for action in actions:
        if action == "noop":
            if cur_round in rounds:
                yield signal * cur_round
            cur_round += 1
        else:
            for i in range(2):
                if cur_round in rounds:
                    yield signal * cur_round
                if i == 1:
                    signal += int(action.split()[1])
                cur_round += 1


def create_crt(actions):
    '''return the crt lines'''
    cur_round = 0
    signal = 1
    crt = [['.' for _ in range(40)] for _ in range(6)]
    for action in actions:
        if action == "noop":
            crt[cur_round//40][cur_round%40] = '#' if cur_round%40 in [signal - 1, signal, signal + 1] else ' '
            cur_round += 1
        else:
            for i in range(2):
                crt[cur_round//40][cur_round%40] = '#' if cur_round%40 in [signal - 1, signal, signal + 1] else ' '
                if i == 1:
                    signal += int(action.split()[1])
                cur_round += 1
    return crt


def read_input():
    '''read the actions of the cpu'''
    with open("input.txt", encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    cpu_actions = read_input()

    # part one
    print(sum(yield_signal_strengths(cpu_actions)))

    # part two
    print(*[''.join(line) for line in create_crt(cpu_actions)], sep="\n")
