import argparse
import importlib

from pathlib import Path
from utils.timeit import timeit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, choices=range(2015, 2025))
    parser.add_argument("day", type=int, choices=range(1, 32))
    args = parser.parse_args()

    day = f"{args.day:02d}"
    year = f"{args.year}"

    file_path = Path() / year / day / f"{day}.py"

    if not file_path.exists():
        print(f"Error: {file_path} does not exist.")
        return
    
    module_name = f"{year}.{day}.{day}"
    try:
        # dynamically define solution functions
        day_module = importlib.import_module(module_name)
        part_one = getattr(day_module, "part_one")
        part_two = getattr(day_module, "part_two")

        # run solutions once to get result
        result_part_one = part_one()
        result_part_two = part_two()

        # run solutions n times to get average time
        time_part_one = timeit(part_one, n=100)
        time_part_two = timeit(part_two, n=100)

        # display results
        print(f"\n--- {year} day {day} ---")
        print(f"Part one: {result_part_one}, {time_part_one}")
        print(f"Part two: {result_part_two}, {time_part_two}")

    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error: Unable to find or import functions from {module_name}: {e}")
    except Exception as e:
        print(f"Unexpected exception: {e}")


if __name__ == "__main__":
    main()
