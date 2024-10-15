#!/usr/bin/env python3
"""Contains async_generator method"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random float values.

    This generator produces 10 random float values between 0 and 10,
    pausing for 1 second between each yield to simulate an asynchronous
    delay.

    Yields:
        float: A random float value between 0 and 10.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
