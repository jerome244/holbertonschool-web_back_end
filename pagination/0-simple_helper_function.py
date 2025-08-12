#!/usr/bin/env python3
"""
Simple helper function to calculate the index range for pagination.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start and end index to paginate the dataset.
    
    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.
    
    Returns:
    tuple: A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
