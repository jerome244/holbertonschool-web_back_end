#!/usr/bin/env python3

"""
This module contains a function 'floor' that takes a float and returns 
the floor of the float.

The function uses the math module to compute the largest integer less 
than or equal to the input float.
"""

import math

def floor(n: float) -> int:
    """
    This function takes a float n as argument and returns the floor of the float.

    Args:
        n (float): The float value for which we need to compute the floor.

    Returns:
        int: The floor of the input float n.
    
    Example:
        >>> floor(3.14)
        3
    """
    return math.floor(n)
