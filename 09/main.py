import itertools


class LinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]
        cur_node = self.head
        for node in nodes[1:]:
            node.prev = cur_node
            cur_node.next = node
            cur_node = cur_node.next


    def __getitem__(self, index):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node)
            node = node.next
        return nodes[index]


class Node:
    def __init__(self, pos_x, pos_y) -> None:
        self.data = (pos_x, pos_y)
        self.next = None
        self.prev = None


def read_route():
    with open("input.txt") as file:
        return [(line.split()[0], int(line.split()[1])) for line in file]


def best_move(first, second):
    f_x, f_y = first
    s_x, s_y = second

    if abs(f_x - s_x) <= 1 and abs(f_y - s_y) <= 1:
        return second

    moves = [*itertools.product([0, 1, -1], repeat=2)][1:]
    move_dist = {(dx, dy): abs(f_x - s_x - dx) + abs(f_y - s_y - dy) for dx, dy in moves}

    best = sorted(move_dist.keys(), key=lambda x: move_dist[x])[0]

    return s_x + best[0], s_y + best[1]


def walk(moves, rope):
    directions = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, 1)}
    path_one, path_two = {(0, 0)}, {(0, 0)}

    for direction, steps in moves:
        d_x, d_y = directions[direction]
        for _ in range(steps):
            rope.head.data = (rope.head.data[0] + d_x, rope.head.data[1] + d_y)
            node = rope.head.next
            while node is not None and node.prev.data is not node.data:
                node.data = best_move(node.prev.data, node.data)
                node = node.next
            path_one.add(rope.head.next.data)
            path_two.add(rope[-1].data)

    return path_one, path_two


if __name__ == '__main__':
    route = read_route()

    linked_rope = LinkedList([Node(0, 0) for _ in range(10)])

    paths = walk(route, linked_rope)

    # part one
    print(len(paths[0]))

    # part two
    print(len(paths[1]))
