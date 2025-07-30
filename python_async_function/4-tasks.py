#!/usr/bin/env python3
""" Tasks """
import asyncio
from typing import List

# Import the task_wait_random function from 3-tasks.py
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronously runs task_wait_random n times and returns the sorted list of delays.

    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): The maximum delay for each wait_random coroutine.

    Returns:
        List[float]: A list of all delays, sorted in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Collect results from tasks as they complete, sorted in the order they are completed
    delays = [await task for task in asyncio.as_completed(tasks)]
    
    return delays
