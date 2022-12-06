import re


def pattern(length):
    return "((\\w)" + "".join(["(" + "".join([f"(?!\\{j})" for j in range(2, i + 1)]) + "\\w)" for i in range(2, length + 1)]) + ")"


def read_stream():
    with open("input.txt") as file:
        return file.readline()


def packet_start(data_stream):
    return re.search(pattern(4), data_stream).end()


def message_start(data_stream):
    return re.search(pattern(14), data_stream).end()


if __name__ == "__main__":
    stream = read_stream()
    print(packet_start(stream))
    print(message_start(stream))
