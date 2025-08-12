#!/usr/bin/env python3
import csv
import math
from typing import List

# Helper function to calculate start and end index
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index for the 
    given page and page_size.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Caches the dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of data from the dataset based on page and page_size."""
        
        # Validate the input values
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."
        
        # Get the dataset
        dataset = self.dataset()
        
        # Get the start and end index for pagination
        start_index, end_index = index_range(page, page_size)
        
        # Return the appropriate page of data or an empty list if the range is out of bounds
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing pagination information and the dataset page."""
        
        # Get the dataset page using get_page
        data = self.get_page(page, page_size)
        
        # Total number of items in the dataset
        total_items = len(self.dataset())
        
        # Total number of pages
        total_pages = math.ceil(total_items / page_size)
        
        # Determine the next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
