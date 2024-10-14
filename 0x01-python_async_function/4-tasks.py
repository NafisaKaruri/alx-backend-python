#!/usr/bin/env python3
"""Contains task_wait_n method"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `task_wait_random` `n` times with the specified `max_delay`.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of wait times in ascending order.
    """
    n_wait_times = await asyncio.gather(
            *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(n_wait_times)
