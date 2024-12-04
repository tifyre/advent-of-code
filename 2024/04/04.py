from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.readlines()
    result = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == "X":
                # out of bounds check
                up, down, left, right = row-3 >= 0, row+3 < len(input), col-3 >= 0, col+3 < len(input[row])
                # vertical
                result += up and input[row-1][col] == "M" and input[row-2][col] == "A" and input[row-3][col] == "S"
                result += down and input[row+1][col] == "M" and input[row+2][col] == "A" and input[row+3][col] == "S"
                # horizontal
                result += left and input[row][col-1] == "M" and input[row][col-2] == "A" and input[row][col-3] == "S"
                result += right and input[row][col+1] == "M" and input[row][col+2] == "A" and input[row][col+3] == "S"
                # diagonal
                result += up and left and input[row-1][col-1] == "M" and input[row-2][col-2] == "A" and input[row-3][col-3] == "S"
                result += up and right and input[row-1][col+1] == "M" and input[row-2][col+2] == "A" and input[row-3][col+3] == "S"
                result += down and left and input[row+1][col-1] == "M" and input[row+2][col-2] == "A" and input[row+3][col-3] == "S"
                result += down and right and input[row+1][col+1] == "M" and input[row+2][col+2] == "A" and input[row+3][col+3] == "S"
    return result


def part_two():
    with open(input_path, "r") as file:
        input = file.readlines()
    result = 0
    for y in range(1, len(input)-1):
        for x in range(1, len(input[y])-1):
            if input[y][x] == "A":
                diagonal1 = f"{input[y-1][x-1]}{input[y][x]}{input[y+1][x+1]}"
                diagonal2 = f"{input[y-1][x+1]}{input[y][x]}{input[y+1][x-1]}"
                if diagonal1 in "MASAM" and diagonal2 in "MASAM":
                    result += 1
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
