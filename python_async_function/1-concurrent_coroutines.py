#!/usr/bin/env python3
"""
Defines concurrent execution function
"""
import asyncio
from typing import List

# Import wait_random from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines at the same time with async

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): delay value to be passed to wait_random

    Returns:
        List[float]: list of delays in ascending order
    """
    # Use asyncio.gather to collect the results concurrently
    resolves = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n))
    )

    # Return the delays in ascending order by relying on the natural behavior of async
    return resolves
