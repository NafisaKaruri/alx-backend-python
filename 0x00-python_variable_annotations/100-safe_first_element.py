#!/usr/bin/env python3
"""Comtains safe_first_element method"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or None."""
    if lst:
        return lst[0]
    else:
        return None
