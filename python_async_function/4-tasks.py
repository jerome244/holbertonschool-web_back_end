#!/usr/bin/env python3
''' async and await syntax '''
import asyncio

# Import wait_random from the previous task
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Function that returns an asyncio Task, which will execute the wait_random coroutine.
    
    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The task that will run the wait_random coroutine.
    '''
    # Create and return an asyncio Task for wait_random
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
