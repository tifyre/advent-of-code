from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def get_trails(grid):  
    potential_trailheads = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 0:
                potential_trailheads.append([x, y])

    trails = []
    for x, y in potential_trailheads:
        valid_paths = []
        explore_around(grid, x, y, valid_paths)
        for path in valid_paths:
            trails.append((x, y, path[0], path[1]))
    return trails


def explore_around(grid, x, y, valid_paths):
    for new_x, new_y in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
        if not 0 <= new_y < len(grid) or not 0 <= new_x < len(grid[y]):
            continue
        if not grid[new_y][new_x] == grid[y][x]+1:
            continue
        if grid[new_y][new_x] == 9:
            valid_paths.append((new_x, new_y))
            continue
        explore_around(grid, new_x, new_y, valid_paths)


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [[int(number) for number in row] for row in input.splitlines()]
    return len(set(get_trails(grid)))


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [[int(number) for number in row] for row in input.splitlines()]
    return len(get_trails(grid))


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
