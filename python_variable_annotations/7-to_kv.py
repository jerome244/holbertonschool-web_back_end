#!/usr/bin/env python3

"""
This module contains a function 'to_kv' that takes a string and an 
integer or float, and returns a tuple where:
- the first element is the string
- the second element is the square of the integer or float, annotated as a float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string k and an integer or float v, and returns 
    a tuple with the string k and the square of v as a float.

    Args:
        k (str): The string to be returned as the first element of the tuple.
        v (Union[int, float]): The integer or float value to be squared 
        and returned as the second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k 
        and the second element is the square of v as a float.

    Example:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)
    """
    return (k, float(v ** 2))
