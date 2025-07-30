#!/usr/bin/env python3
"""
Defines an async comprehension over an async generator.
"""
from typing import List

# Import async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    # Use async comprehension to collect 10 random numbers
    return [num async for num in async_generator()]
