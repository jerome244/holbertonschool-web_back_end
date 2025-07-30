#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence from the iterable and the length of that sequence.

    Args:
        lst (Iterable[Sequence]): An iterable where each element is a sequence 
        (e.g., string, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains 
        a sequence and its length.
    
    Example:
        >>> element_length(["hello", (1, 2, 3), [1, 2, 3, 4]])
        [('hello', 5), ((1, 2, 3), 3), ([1, 2, 3, 4], 4)]
    """
    return [(i, len(i)) for i in lst]
