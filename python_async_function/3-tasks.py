#!/usr/bin/env python3

"""
This module defines the function `task_wait_random` which creates an asyncio task 
for the `wait_random` coroutine and returns it as an asyncio.Task object.
"""

import asyncio
from wait_random import wait_random  # Import wait_random from the previous file

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task to execute the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The task representing the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
