import re


# regex pattern for console logs
folder_in_pattern = r'(\$ cd [a-z]+)|(\$ cd \/)'
folder_out_pattern = r'(\$ cd \.\.)'
file_pattern = r'[0-9]+ [a-z]+'


def read_console():
    with open("input.txt") as file:
        return [line for line in file.readlines()]


def init_folder_dict(console):
    folder_size = {}
    path = []
    for line in console:
        if re.match(folder_in_pattern, line):
            path.append(line.split()[-1])
        elif re.match(folder_out_pattern, line):
            path.pop()
        elif re.match(file_pattern, line):
            for i in range(len(path)):
                if '/'.join(path[:i+1]) in folder_size.keys():
                    folder_size['/'.join(path[:i+1])] += int(line.split()[0])
                else:
                    folder_size['/'.join(path[:i+1])] = int(line.split()[0])
    return folder_size


if __name__ == "__main__":
    console_logs = read_console()
    folder_dict = init_folder_dict(console_logs)

    # part one
    print(sum(value for value in folder_dict.values() if value <= 100000))

    # part two
    print(min(value for value in folder_dict.values() if value >= folder_dict['/'] - 40000000))
