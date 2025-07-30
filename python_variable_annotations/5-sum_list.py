#!/usr/bin/env python3

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns their sum as a float.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the floats in the input_list.

    Example:
        >>> sum_list([3.14, 1.11, 2.22])
        6.47
    """
    return sum(input_list)
