#!/usr/bin/env python3

import asyncio
from wait_random import wait_random  # Import the previous wait_random coroutine

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to use for the wait_random coroutine.

    Returns:
        asyncio.Task: The task representing the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
