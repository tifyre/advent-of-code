import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def solution():
    return


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    result = sum([int(x) * int(y) for x, y in matches])
    return result


def part_two():
    return


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
