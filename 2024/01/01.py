from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def parse_input():
    with open(input_path, "r") as file:
        input = file.readlines()

    lefts, rights = [], []
    for row in input:
        left, right = row.split()
        lefts.append(int(left))
        rights.append(int(right))

    return sorted(lefts), sorted(rights)


def part_one():
    lefts, rights = parse_input()
    return sum([abs(left - right) for left, right in zip(lefts, rights)])


def part_two():
    lefts, rights = parse_input()
    return sum([left * rights.count(left) for left in lefts])


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
