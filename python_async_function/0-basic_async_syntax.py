#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    This coroutine waits for a random delay between 0 and max_delay (inclusive),
    and returns the delay in seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay between 0 and max_delay (inclusive).
    
    Example:
        >>> await wait_random(5)
        2.3456
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
