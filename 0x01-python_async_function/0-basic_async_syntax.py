#!/usr/bin/env python3
"""Contains wait_random method"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and `max_delay`.

    Args:
        max_delay (int): The maximum delay (default is 10).

    Returns:
        float: The actual wait time for the delay.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
