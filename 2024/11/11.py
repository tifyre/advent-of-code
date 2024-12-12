from collections import Counter
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def blink(stone:str):
    """take a single stone and return a list of what it would be after blinking"""
    if stone == "0":
        return ["1"]
    if len(stone) % 2 == 0:
        return[stone[:len(stone)//2], str(int(stone[len(stone)//2:]))]
    return [str(int(stone) * 2024)]


def solve(stones:list, n_blinks):
    counts = dict(Counter(stones))
    new_counts = {}
    for _ in range(n_blinks):
        for stone, count in counts.items():
            post_blink = blink(stone)
            for new_stone in post_blink:
                if new_stone not in new_counts:
                    new_counts[new_stone] = count
                else:
                    new_counts[new_stone] += count
        counts = new_counts
        new_counts = {}
    return sum(counts.values())


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    stones = input.split()
    return solve(stones, n_blinks=25)


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    stones = input.split()
    return solve(stones, n_blinks=75)


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
