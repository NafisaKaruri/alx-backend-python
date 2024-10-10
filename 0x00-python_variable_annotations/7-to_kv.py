#!/usr/bin/env python3
"""Contain to_kv method"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of the int/float."""
    return (k, float(v ** 2))
