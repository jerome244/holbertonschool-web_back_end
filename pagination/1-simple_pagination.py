#!/usr/bin/env python3
import csv
import math
from typing import List


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
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of data from the dataset based on page and page_size."""

        # Assert that page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get the dataset
        dataset = self.dataset()

        # Calculate the start and end index using index_range
        start_index, end_index = index_range(page, page_size)

        # If the requested page is out of range, return an empty list
        if start_index >= len(dataset):
            return []
        
        # Return the sliced dataset page
        return dataset[start_index:end_index]
