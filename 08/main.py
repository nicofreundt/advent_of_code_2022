import math


def tree_grid():
    with open("input.txt") as file:
        return [[*map(int, line.strip())] for line in file.readlines()]


def is_visible(x, y, grid):
    element = grid[x][y]
    row = grid[x]
    col = [r[y] for r in grid]
    b_row = max(row[:y]+[-1])
    a_row = max(row[y+1:]+[-1])
    b_col = max(col[:x]+[-1])
    a_col = max(col[x+1:]+[-1])
    return any(i < element for i in [b_row, a_row, b_col, a_col])


def scenic_score(x, y, grid):
    element = grid[x][y]
    row = grid[x]
    col = [r[y] for r in grid]
    b_row = row[:y][::-1]
    a_row = row[y+1:]
    b_col = col[:x][::-1]
    a_col = col[x+1:]
    return math.prod(min([i for i, tree in enumerate(trees) if tree >= element]) + 1 if any(tree >= element for tree in trees) else len(trees) for trees in [b_row, a_row, b_col, a_col])


if __name__ == "__main__":
    grid_of_trees = tree_grid()

    # part one
    print(sum(sum(is_visible(x, y, grid_of_trees) for y in range(len(grid_of_trees[x]))) for x in range(len(grid_of_trees))))

    # part two
    print(max(max(scenic_score(x, y, grid_of_trees) for y in range(len(grid_of_trees[x]))) for x in range(len(grid_of_trees))))
