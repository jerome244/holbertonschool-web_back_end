#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as an argument and returns a function 
    that multiplies a float by the multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float as input and 
        returns the result of multiplying it by the multiplier.

    Example:
        >>> multiplier_by_2 = make_multiplier(2)
        >>> multiplier_by_2(3)
        6
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    
    return multiplier_function
