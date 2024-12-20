#!/usr/bin/env python3
"""Contains safely_get_value method"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Return the value associated with key or default."""
    if key in dct:
        return dct[key]
    else:
        return default
