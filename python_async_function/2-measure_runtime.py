#!/usr/bin/env python3

import asyncio
import time
from wait_random import wait_n  # Import the previous wait_n coroutine

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for the wait_n coroutine and return
    the average time per execution.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay to use for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.perf_counter()  # Start time measurement
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.perf_counter()  # End time measurement

    total_time = end_time - start_time  # Calculate total execution time
    return total_time / n  # Return average time per coroutine
