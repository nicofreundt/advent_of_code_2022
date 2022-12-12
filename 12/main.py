"""Pathfinding - Advent of Code Day 12"""


def read_grid():
    '''read grid from file'''
    with open("input.txt", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]


def find_path_length(start_points, end_point, grid):
    '''calculate the path length'''
    checkable_points = [(start_point, 0) for start_point in start_points]
    checked_points = set()
    cur_point, cur_dist = (0, 0), 0
    while cur_point != end_point:
        cur_point, cur_dist = checkable_points.pop(0)
        checked_points.add(cur_point)
        checkable_points = [*filter(lambda x: x[0] not in checked_points, checkable_points + [(neighbour, cur_dist+1) for neighbour in [*filter(lambda x: x[0] in range(len(grid)) and x[1] in range(len(grid[0])) and grid[x[0]][x[1]] <= 1 + grid[cur_point[0]][cur_point[1]], [(cur_point[0] + move[0], cur_point[1] + move[1]) for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]])]])]
    return cur_dist


if __name__ == "__main__":
    matrix = read_grid()

    start = [(x, line.index('S'))
             for x, line in enumerate(matrix) if 'S' in line]
    end = [(x, line.index('E'))
           for x, line in enumerate(matrix) if 'E' in line].pop()

    matrix = [[ord(char) - 96 if char not in ['S', 'E'] else {'S': 1, 'E': 26}.get(char) for char in line] for line in matrix]

    # part one
    print(find_path_length(start, end, matrix))

    # part two
    start = [(x, line.index(1)) for x, line in enumerate(matrix) if 1 in line]
    print(find_path_length(start, end, matrix))
