#!/usr/bin/env python3

"""
This module contains a function 'concat' that concatenates two strings
and returns the resulting string.

The function takes two string arguments and joins them into one string.
"""

def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    Args:
        str1 (str): The first string to be concatenated.
        str2 (str): The second string to be concatenated.

    Returns:
        str: The concatenated string formed by joining str1 and str2.
    
    Example:
        >>> concat("egg", "shell")
        'eggshell'
    """
    return str1 + str2
