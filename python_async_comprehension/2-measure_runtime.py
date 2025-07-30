#!/usr/bin/env python3
"""
Measures the total runtime for running four parallel async comprehensions.
"""
import asyncio
import time
from typing import List

# Import async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension four times in parallel.

    Returns:
        float: The total runtime of all four executions in seconds.
    """
    start_time = time.perf_counter()  # Capture the start time
    # Execute async_comprehension four times concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()  # Capture the end time
    total_time = end_time - start_time  # Calculate the total runtime
    return total_time  # Return the total time
