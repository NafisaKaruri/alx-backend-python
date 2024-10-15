#!/usr/bin/env python3
"""Contains async_comprehension method"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects random float values.

    This function utilizes the async_generator to gather random float values
    into a list. It runs the generator asynchronously and collects the results
    using an asynchronous list comprehension.

    Returns:
        List[float]: list of random float values yielded by the async_generator
    """
    return [_ async for _ in async_generator()]
