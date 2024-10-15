#!/usr/bin/env python3
"""Contains measure_runtime method"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of four parallel async_comprehension calls.

    This coroutine executes async_comprehension four times concurrently
    using asyncio.gather and measures the total time taken for all calls
    to complete.

    Returns:
        float: Total runtime for executing the async_comprehension four times.
    """
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    return time.time() - start_time
