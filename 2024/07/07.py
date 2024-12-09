from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    orders, updates = input.split("\n\n")
    orders = orders.split()
    updates = updates.split()

    seen = {}
    for order in orders:
        key, value = order.split("|")
        if key not in seen:
            seen[key] = [value]
        else:
            seen[key].append(value)

    result = 0
    for update in updates:
        valid = True
        update = update.split(",")
        for i in range(1, len(update)):
            if update[i] not in seen[update[i-1]]:
                valid = False
                break
        if valid:
            result += int(update[len(update) // 2])

    return result


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    orders, updates = input.split("\n\n")
    orders = orders.split()
    updates = updates.split()

    seen = {}
    for order in orders:
        key, value = order.split("|")
        if key not in seen:
            seen[key] = [value]
        else:
            seen[key].append(value)

    result = 0
    for update in updates:
        valid = True
        update = update.split(",")
        for i in range(1, len(update)):
            if update[i] not in seen[update[i-1]]:
                valid = False
                break
        if valid:
            continue

        counts = {}
        for i, value in enumerate(update):
            counts[value] = 0
            for other_value in update[:i] + update[i+1:]:
                if other_value in seen[value]:
                    counts[value] += 1
        sorted_update = sorted(update, key=lambda item: counts[item], reverse=True)
        result += int(sorted_update[len(sorted_update) // 2])

    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
