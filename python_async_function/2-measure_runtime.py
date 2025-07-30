#!/usr/bin/env python3

"""
This module defines the function `measure_time` which measures the total execution
time for the `wait_n` coroutine and returns the average time per execution.
"""

import asyncio
import time
from wait_n import wait_n  # Import wait_n from the previous file

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the wait_n coroutine and returns
    the average time per execution.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    return total_time / n
