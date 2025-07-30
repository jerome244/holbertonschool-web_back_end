#!/usr/bin/env python3

"""
This module contains a function 'to_str' that takes a float and returns 
its string representation.

The function uses the built-in str() function to convert the float into 
a string format.
"""

def to_str(n: float) -> str:
    """
    This function takes a float n as argument and returns its string 
    representation.

    Args:
        n (float): The float value to be converted into a string.

    Returns:
        str: The string representation of the input float n.
    
    Example:
        >>> to_str(3.14)
        '3.14'
    """
    return str(n)
