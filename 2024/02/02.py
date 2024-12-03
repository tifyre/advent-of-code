from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def is_valid(report):
    increasing = report[0] < report[1]
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if not (1 <= abs(diff) <= 3):
            return False
        if increasing and diff < 0:
            return False
        if not increasing and diff > 0:
            return False
    return True


def recursive(report, tolerance, errors=0):
    if is_valid(report):
        return True
    
    errors += 1
    if errors > tolerance:
        return False
    
    for i in range(len(report)):
        modified_report = report[:i]+report[i+1:]
        if recursive(modified_report, tolerance, errors):
            return True
    return False


def solution(tolerance):
    with open(input_path, "r") as file:
        input = file.read()
    result = 0
    reports = input.splitlines()
    for report in reports:
        report = [int(line) for line in report.split()]
        result += recursive(report, tolerance)
    return result


def part_one():
    return solution(tolerance=0)


def part_two():
    return solution(tolerance=1)


if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
