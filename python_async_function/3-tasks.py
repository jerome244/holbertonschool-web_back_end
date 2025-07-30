#!/usr/bin/env python3
"""
Defines runtime of an asynchronous function.
"""
import time
import asyncio

# Import wait_n from the previous task
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the time it takes to execute `wait_n` n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn the wait_random coroutine.
        max_delay (int): The maximum delay to be passed to the wait_random coroutine.

    Returns:
        float: The average time taken per coroutine execution in seconds.
    """
    start: float = time.time()  # Capture the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end: float = time.time()  # Capture the end time
    total_time: float = end - start  # Calculate the total execution time
    
    # Return the average time per coroutine
    return total_time / n  # Return average execution time per coroutine
