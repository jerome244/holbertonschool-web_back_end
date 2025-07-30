#!/usr/bin/env python3

"""
This module defines a coroutine `task_wait_n` that spawns `n` instances of the 
`task_wait_random` function with the specified `max_delay` and returns a list 
of delays in ascending order.
"""

import asyncio
from task_wait_random import task_wait_random  # Import the task_wait_random function

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    This coroutine spawns `n` instances of the task_wait_random function with
    the specified `max_delay` and returns a list of delays in ascending order.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        list: A list of the random delays, sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return completed_delays
