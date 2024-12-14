import re
from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def forward_one_second(robots, width, height):
    for robot in robots:
        x, y, x_vel, y_vel = robot.values()
        new_x, new_y = x + x_vel, y + y_vel
        robot["x"] = width + new_x if new_x < 0 else new_x - width if new_x >= width else new_x
        robot["y"] = height + new_y if new_y < 0 else new_y - height if new_y >= height else new_y


def part_one():
    with open(input_path, "r") as file:
        data = file.read()

    width, height = 101, 103
    robots = []
    for line in data.split("\n"):
        x, y, x_vel, y_vel = list(map(int, re.findall(r'-?\d+', line)))
        robots.append({"x": x, "y": y, "x_vel": x_vel, "y_vel": y_vel})

    for _ in range(100):
        forward_one_second(robots, width, height)

    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        x, y = robot["x"], robot["y"]
        x_mid, y_mid = width//2, height//2
        if x < x_mid and y < y_mid:
            q1 += 1
        elif x > x_mid and y < y_mid:
            q2 += 1
        elif x < x_mid and y > y_mid:
            q3 += 1
        elif x > x_mid and y > y_mid:
            q4 += 1
    return q1 * q2 * q3 * q4


def part_two():
    with open(input_path, "r") as file:
        data = file.read()

    width, height = 101, 103
    robots = []
    for line in data.split("\n"):
        x, y, x_vel, y_vel = list(map(int, re.findall(r'-?\d+', line)))
        robots.append({"x": x, "y": y, "x_vel": x_vel, "y_vel": y_vel})
    
    fill_char = "X"
    result = 0
    while True:
        result += 1
        print_this = False
        grid = [[" "] * width for _ in range(height)]

        forward_one_second(robots, width, height)
        for robot in robots:
            x, y = robot["x"], robot["y"]
            grid[y][x] = fill_char
        for row in grid:
            if row.count(fill_char) > 20:
                print_this = True
                break

        if print_this:
            for row in grid:
                print("".join(row))
            if input():
                break
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
