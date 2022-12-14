"""Advent of Code Day 14"""


def read_cave():
    '''read 2D representation of cave'''
    with open("input.txt", encoding="utf-8") as file:
        paths = [[{'x': x, 'y': y} for x, y in [map(int, point.split(',')[::-1]) for point in line.strip().split(' -> ')]] for line in file.readlines()]
        max_x = max(max(point['x'] for point in path) for path in paths) + 1
        max_y = max(max(point['y'] for point in path) for path in paths) + 1
        grid = [['.' for _ in range(max_y*2)] for _ in range(max_x+2)]
        for path in paths:
            for path_ix in range(len(path)-1):
                for row in range(min(path[path_ix]['x'], path[path_ix+1]['x']), max(path[path_ix]['x'], path[path_ix+1]['x']) + 1):
                    for column in range(min(path[path_ix]['y'], path[path_ix+1]['y']), max(path[path_ix]['y'], path[path_ix+1]['y']) + 1):
                        grid[row][column] = '#'
        grid[0][500] = '+'
        return grid


def spawn_sand(grid, row=0, col=500):
    '''spawn new sand'''
    while row + 1 < len(grid) and grid[row + 1][col] == '.':
        row += 1
    if row >= len(grid) - 1 or grid[0][500] == 'o':
        return False
    if grid[row + 1][col - 1] in ['#', 'o'] and grid[row + 1][col + 1] in ['#', 'o']:
        grid[row][col] = 'o'
        return True
    return spawn_sand(grid, row, col - 1) if grid[row + 1][col - 1] == '.' else spawn_sand(grid, row, col + 1)


if __name__ == "__main__":
    cave = read_cave()

    # part one
    sand = spawn_sand(cave)
    count = 0
    while sand:
        count += 1
        sand = spawn_sand(cave)
    print(count)

    # part two
    for i in range(len(cave[-1])):
        cave[-1][i] = '#'
    sand = spawn_sand(cave)
    while sand:
        count += 1
        sand = spawn_sand(cave)
    print(count)
