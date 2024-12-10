from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.read()

    blocks = []
    for i, char in enumerate(input):
        if i % 2 == 0:
            blocks += [str(i//2)] * int(char)
        else:
            blocks += "." * int(char)

    i, j = 0, len(blocks)-1
    while i < j:
        if blocks[i] != ".":
            i += 1
            continue
        if blocks[j] == ".":
            j -= 1
            continue
        blocks[i] = blocks[j]
        blocks[j] = "."
        i += 1
        j -= 1

    result = 0
    for i, char in enumerate(blocks):
        if char == ".":
            break
        result += int(char) * i
    return result


def part_two():
    with open(input_path, "r") as file:
        input = file.read()

    blocks = []
    for j, char in enumerate(input):
        if j % 2 == 0:
            blocks += [str(j//2)] * int(char)
        else:
            blocks += "." * int(char)

    i = len(blocks)-1
    while 0 < i:
        if blocks[i] == ".":
            i -= 1
            continue

        a = i
        while a > 0 and blocks[a-1] == blocks[i]:
            a -= 1
        block = blocks[a:i+1]

        for j in range(len(blocks)):
            if j > i:
                break
            if blocks[j] != ".":
                continue
            b = j
            while b < len(blocks)-1 and blocks[b+1] == ".":
                b += 1
            if b+1-j >= len(block):
                blocks[j:j+len(block)] = block
                blocks[a:i+1] = ["."] * len(block)
                break
        i -= len(block)

    result = 0
    for j, char in enumerate(blocks):
        if char == ".":
            continue
        result += int(char) * j
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
