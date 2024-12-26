from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.read()

    keys, locks = [], []
    items = input.split("\n\n")
    for item in items:
        cols = [-1] * 5
        for line in item.splitlines():
            for i, char in enumerate(line):
                cols[i] += 1 if char == "#" else 0
        if item.startswith("....."):
            keys.append(cols)
        else:
            locks.append(cols)

    result = 0
    for key in keys:
        for lock in locks:
            fitting = True
            for i, count in enumerate(key):
                if lock[i] + count > 5:
                    fitting = False
                    break
            if not fitting:
                continue
            result += 1
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
