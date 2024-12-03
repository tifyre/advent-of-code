import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    result = sum([int(x) * int(y) for x, y in matches])
    return result


def part_two():
    with open(input_path, "r") as file:
        input = file.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|\b(do|don't)\(\)"
    matches = re.finditer(pattern, input)

    do = True
    result = 0
    for match in matches:
        instruction = match.group()
        if instruction.startswith("mul") and do:
            result += int(match.group(1)) * int(match.group(2))
        elif instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
