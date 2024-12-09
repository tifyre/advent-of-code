from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [list(row) for row in input.split()]

    facing = 0
    for y, row in enumerate(grid):
        if "^" in row:
            pos = [row.index("^"), y]
            break

    visited = [pos]
    while True:
        y_move = -1 if facing == 0 else 1 if facing == 2 else 0
        x_move = -1 if facing == 3 else 1 if facing == 1 else 0
        x, y = pos[0] + x_move, pos[1] + y_move

        if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
            break

        if grid[y][x] == "#":
            facing = (facing + 1) % 4
            continue
        
        pos = [x, y]
        if pos not in visited:
            visited.append(pos)
    
    return len(visited)


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [list(row) for row in input.split()]

    facing = 0
    for y, row in enumerate(grid):
        if "^" in row:
            pos = [row.index("^"), y]
            break

    visited = [pos]
    facings = [facing]
    while True:
        y_move = -1 if facing == 0 else 1 if facing == 2 else 0
        x_move = -1 if facing == 3 else 1 if facing == 1 else 0
        x, y = pos[0] + x_move, pos[1] + y_move

        if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
            break

        if grid[y][x] == "#":
            facing = (facing + 1) % 4
            continue
        
        pos = [x, y]
        if pos not in visited:
            visited.append(pos)
            facings.append(facing)

    result = 0
    for (i, pos), facing in zip(enumerate(visited[:-1]), facings[:-1]):
        grid_copy = [list(l) for l in grid]
        grid_copy[visited[i+1][1]][visited[i+1][0]] = "#"

        new_visited = [pos + [facing]]
        while True:
            y_move = -1 if facing == 0 else 1 if facing == 2 else 0
            x_move = -1 if facing == 3 else 1 if facing == 1 else 0
            x, y = pos[0] + x_move, pos[1] + y_move

            if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
                break

            if grid_copy[y][x] == "#":
                facing = (facing + 1) % 4
            else:
                pos = [x, y]

            if pos + [facing] in new_visited:
                result += 1
                break
            new_visited.append(pos + [facing])
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
