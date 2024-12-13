import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def tokens_required(machines, unit_correction=0):
    tokens = 0
    for machine in machines:
        b1x, b1y, b2x, b2y, X, Y = list(map(int, re.findall(r'\d+', machine)))

        X += unit_correction
        Y += unit_correction

        A = b1x * b2y - b1y * b2x
        Ax = X * b2y - Y * b2x
        Ay = b1x * Y - b1y * X

        if A == 0:
            continue

        times_b1 = Ax / A
        times_b2 = Ay / A

        if int(times_b1) != times_b1 or int(times_b2) != times_b2:
            continue

        tokens += int(times_b1) * 3 + int(times_b2)
    return tokens


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    machines = input.split("\n\n")
    return tokens_required(machines)


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    machines = input.split("\n\n")
    return tokens_required(machines, 10000000000000)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
