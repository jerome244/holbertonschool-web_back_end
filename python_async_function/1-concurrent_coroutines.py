#!/usr/bin/env python3

import asyncio
from typing import List
from wait_random import wait_random  # Import the previous coroutine

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This coroutine spawns `n` instances of the `wait_random` coroutine with 
    the specified `max_delay`. It returns a list of delays in ascending order.
    
    Args:
        n (int): The number of coroutines to run.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: A list of the random delays, sorted in ascending order.
    """
    # Run all the wait_random coroutines concurrently
    delays = [wait_random(max_delay) for _ in range(n)]
    
    # Gather the results from all the coroutines
    completed_delays = await asyncio.gather(*delays)
    
    # Return the completed delays in ascending order
    return completed_delays
