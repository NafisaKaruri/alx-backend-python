#!/usr/bin/env python3
"""Contains wait_n method"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` `n` times with the specified `max_delay`.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for each wait.

    Returns:
        List[float]: A list of wait times in ascending order.
    """
    n_wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(n_wait_times)
