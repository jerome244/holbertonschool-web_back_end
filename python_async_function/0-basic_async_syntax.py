#!/usr/bin/env python3
"""
Defines a basic asynchronous routine that waits for a random delay
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay between 0 and max_delay
    (inclusive) seconds and returns the delay time.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
