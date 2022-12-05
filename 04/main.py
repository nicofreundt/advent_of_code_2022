def read_range_pairs():
    with open("input.txt") as file:
        return [[{'min': int(r.split('-')[0]), 'max': int(r.split('-')[1])} for r in line.split(',')] for line in file.readlines()]


def count_range_subsets(range_pairs):
    return sum([(range_a := set(range(pair[0]['min'], pair[0]['max'] + 1))).issubset(range_b := set(range(pair[1]['min'], pair[1]['max'] + 1))) or range_a.issuperset(range_b) for pair in range_pairs])


def count_range_overlapping(range_pairs):
    return sum([not set(range(pair[0]['min'], pair[0]['max'] + 1)).isdisjoint(set(range(pair[1]['min'], pair[1]['max'] + 1))) for pair in range_pairs])


if __name__ == "__main__":
    # part one
    print(count_range_subsets(read_range_pairs()))

    # part two
    print(count_range_overlapping(read_range_pairs()))
