from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def parse_input(input:str):
    grid = [list(line) for line in input.splitlines()]
    for i, row in enumerate(grid):
        if "S" in row:
            start = [row.index("S"), i]
            break
    return grid, start


def neighbors(x, y, grid):
    next_steps = []
    if y+1 < len(grid):
        next_steps.append([x, y+1])
    if y-1 >= 0:
        next_steps.append([x, y-1])
    if x+1 < len(grid[0]):
        next_steps.append([x+1, y])
    if x-1 >= 0:
        next_steps.append([x-1, y])
    return next_steps


def get_path(grid, start):
    seen = []
    queue = [[start, 0, [start]]]
    while queue:
        (x, y), steps, path = queue.pop(0)
        token = grid[y][x]
        if token == "E":
            break
        seen.append([x, y])
        for next in neighbors(x, y, grid):
            if grid[next[1]][next[0]] == "#":
                continue
            if next in seen:
                continue
            queue.append([next, steps+1, path + [next]])
    return path


def get_cheats(path, max_steps, need_to_save=100):
    result = 0
    for i, a in enumerate(path[:-(need_to_save+1)]):
        for j, b in enumerate(path[i+need_to_save-1::]):
            steps_taken = abs(a[0]-b[0]) + abs(a[1]-b[1])
            if j <= steps_taken:
                continue
            if steps_taken > max_steps:
                continue
            result += 1
    return result


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    grid, start = parse_input(input)
    path = get_path(grid, start)
    return get_cheats(path, max_steps=2)


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    grid, start = parse_input(input)
    path = get_path(grid, start)
    return get_cheats(path, max_steps=20)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
