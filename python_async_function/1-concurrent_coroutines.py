#!/usr/bin/env python3

"""
This module defines a coroutine `wait_n` that spawns multiple `wait_random`
coroutines concurrently and returns a list of delays in ascending order.
"""

import asyncio
from wait_random import wait_random  # Import wait_random from the previous file

async def wait_n(n: int, max_delay: int) -> list:
    """
    This coroutine spawns `n` instances of the wait_random coroutine with 
    the specified `max_delay`. It returns a list of delays in ascending order.

    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        list: A list of the random delays, sorted in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*delays)
    return completed_delays
