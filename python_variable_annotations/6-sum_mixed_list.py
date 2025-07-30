#!/usr/bin/env python3

"""
This module contains a function 'sum_mixed_list' that takes a list of
integers and floats, and returns their sum as a float.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats and returns their sum 
    as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing both integers 
        and floats to be summed.

    Returns:
        float: The sum of the integers and floats in the list.

    Example:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        679.13
    """
    return float(sum(mxd_lst))
