#!/usr/bin/env python3
"""Simple helper function index range"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of start and end index to paginate the dataset.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        Tuple[int, int]: A tuple containing the start and end indices for the pagination.
    """
    start_index = page_size * (page - 1)  # Calculate the start index
    end_index = start_index + page_size  # Calculate the end index
    return (start_index, end_index)
