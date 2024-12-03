import time

def timeit(test_function, n=1):
        # run function n times and average time
        start_time = time.time_ns()
        for _ in range(n):
            test_function()
        time_ns = (time.time_ns() - start_time) / n

        time_units = [
            (1_000_000_000, "s"),  # seconds
            (1_000_000, "ms"),  # milliseconds
            (1_000, "µs"),  # microseconds
            (1, "ns")  # nanoseconds
        ]

        # return time scaled to appropriate unit
        for unit_size, unit_name in time_units:
            if time_ns >= unit_size:
                return f"{time_ns/unit_size:.2f}{unit_name}"
