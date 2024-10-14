#!/usr/bin/env python3
"""Contains meature_time method"""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of the wait_n coroutine.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each wait.

    Returns:
        float: The average time per call to wait_n, in seconds.
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    return(time() - start) / n
