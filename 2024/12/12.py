from pathlib import Path

input_path = Path(__file__).parent / "input.txt"


def count_corners(grid, x, y):
    tl = (x-1, y-1)
    tm = (x, y-1)
    tr = (x+1, y-1)
    ml = (x-1, y)
    mr = (x+1, y)
    bl = (x-1, y+1)
    bm = (x, y+1)
    br = (x+1, y+1)

    if 0 <= tl[0] < len(grid) and 0 <= tl[1] < len(grid[tl[0]]):
        tl = grid[tl[1]][tl[0]]
    if 0 <= tm[0] < len(grid) and 0 <= tm[1] < len(grid[tm[0]]):
        tm = grid[tm[1]][tm[0]]
    if 0 <= tr[0] < len(grid) and 0 <= tr[1] < len(grid[tr[0]]):
        tr = grid[tr[1]][tr[0]]
    if 0 <= ml[0] < len(grid) and 0 <= ml[1] < len(grid[ml[0]]):
        ml = grid[ml[1]][ml[0]]
    if 0 <= mr[0] < len(grid) and 0 <= mr[1] < len(grid[mr[0]]):
        mr = grid[mr[1]][mr[0]]
    if 0 <= bl[0] < len(grid) and 0 <= bl[1] < len(grid[bl[0]]):
        bl = grid[bl[1]][bl[0]]
    if 0 <= bm[0] < len(grid) and 0 <= bm[1] < len(grid[bm[0]]):
        bm = grid[bm[1]][bm[0]]
    if 0 <= br[0] < len(grid) and 0 <= br[1] < len(grid[br[0]]):
        br = grid[br[1]][br[0]]

    char = grid[y][x]
    count = 0

    if all(pos != char for pos in [tm, ml, mr, bm]):
        count += 4
    if tm == char and all(pos != char for pos in [ml, mr, bm]):
        count += 2
    if mr == char and all(pos != char for pos in [tm, ml, bm]):
        count += 2
    if bm == char and all(pos != char for pos in [tm, ml, mr]):
        count += 2
    if ml == char and all(pos != char for pos in [tm, mr, bm]):
        count += 2
    if all(pos == char for pos in [tm, ml]) and all(pos != char for pos in [tl]):
        count += 1
    if all(pos == char for pos in [tm, mr]) and all(pos != char for pos in [tr]):
        count += 1
    if all(pos == char for pos in [mr, bm]) and all(pos != char for pos in [br]):
        count += 1
    if all(pos == char for pos in [ml, bm]) and all(pos != char for pos in [bl]):
        count += 1
    if all(pos == char for pos in [tm, ml]) and all(pos != char for pos in [mr, bm]):
        count += 1
    if all(pos == char for pos in [tm, mr]) and all(pos != char for pos in [ml, bm]):
        count += 1
    if all(pos == char for pos in [mr, bm]) and all(pos != char for pos in [tm, ml]):
        count += 1
    if all(pos == char for pos in [ml, bm]) and all(pos != char for pos in [tm, mr]):
        count += 1
    return count


def search_around_part_one(grid, x, y, borders, region):
    region.append((x, y))
    char = grid[y][x]
    for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if not 0 <= new_y < len(grid) or not 0 <= new_x < len(grid[new_y]):
            borders.append([x, y, new_x, new_y])
            continue
        if not [x, y, new_x, new_y] in borders and not [new_x, new_y, x, y] in borders and grid[y][x] != grid[new_y][new_x]:
            borders.append([x, y, new_x, new_y])
        if grid[new_y][new_x] == char and (new_x, new_y) not in region:
            search_around_part_one(grid, new_x, new_y, borders, region)


def search_around_part_two(grid, x, y, region, checked_corners=[], count=0):
    if (x, y) not in checked_corners:
        checked_corners.append((x, y))
        count += count_corners(grid, x, y)
    region.append((x, y))
    char = grid[y][x]
    for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if not 0 <= new_y < len(grid) or not 0 <= new_x < len(grid[new_y]):
            continue
        if grid[new_y][new_x] != char:
            continue
        if (new_x, new_y) in region:
            continue
        count = search_around_part_two(grid, new_x, new_y, region, checked_corners, count)
    return count


def part_one():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [list(row) for row in input.split()]
    visited = []
    result = 0
    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[y]):
            if (x, y) in visited:
                continue
            borders, region = [], []
            search_around_part_one(grid, x, y, borders, region)
            visited.extend(region)
            result += len(borders) * len(region)
    return result


def part_two():
    with open(input_path, "r") as file:
        input = file.read()
    grid = [list(row) for row in input.split()]
    visited = []
    result = 0
    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[y]):
            if (x, y) in visited:
                continue
            region = []
            corners = search_around_part_two(grid, x, y, region)
            result += corners * len(region)
            visited.extend(region)
    return result


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
