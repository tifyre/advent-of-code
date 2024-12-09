from itertools import permutations
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
    

def part_one():
    with open(input_path, "r") as file:
        input = file.readlines()
    grid = [list(row.strip()) for row in input]

    memory = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "." or char == "#":
                continue
            elif char not in memory:
                memory[char] = [(x, y)]
            else:
                memory[char].append((x, y))
    
    results = []
    for positions in memory.values():
        for pair in permutations(positions, 2):
            pos1, pos2 = pair
            x = pos1[0] + (pos1[0] - pos2[0])
            y = pos1[1] + (pos1[1] - pos2[1])
            if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
                continue
            if [x, y] not in results:
                results.append([x, y])
    return len(results)


def part_two():
    with open(input_path, "r") as file:
        input = file.readlines()
    grid = [list(row.strip()) for row in input]

    memory = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "." or char == "#":
                continue
            elif char not in memory:
                memory[char] = [(x, y)]
            else:
                memory[char].append((x, y))
    
    results = []
    for positions in memory.values():
        for pair in permutations(positions, 2):
            pos1, pos2 = pair
            x, y = pos1[0], pos1[1]
            x_diff, y_diff = pos1[0] - pos2[0], pos1[1] - pos2[1]
            while True:
                if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
                    break
                if [x, y] not in results:
                    results.append([x, y])
                x += x_diff
                y += y_diff
    return len(results)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
