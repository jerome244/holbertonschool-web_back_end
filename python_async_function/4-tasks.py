#!/usr/bin/env python3

import asyncio
from task_wait_random import task_wait_random  # Import the task_wait_random function

async def task_wait_n(n: int, max_delay: int) -> list:
    """
    This coroutine spawns `n` instances of the task_wait_random function with 
    the specified `max_delay` and returns a list of delays in ascending order.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay to use for each coroutine.

    Returns:
        list: A list of the random delays, sorted in ascending order.
    """
    # Create a list of asyncio Tasks by calling task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Wait for all the tasks to complete and get the results
    completed_delays = await asyncio.gather(*tasks)
    
    # Return the delays in ascending order
    return completed_delays
