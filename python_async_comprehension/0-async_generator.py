#!/usr/bin/env python3
"""
Defines an asynchronous generator that yields random numbers.
"""
import asyncio
import random

async def async_generator() -> float:
    """
    Asynchronous generator that yields a random float between 0 and 10 
    after waiting 1 second each time.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
