#!/usr/bin/env python3
""" Pymongo """

from typing import List
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[dict]:
    """List all documents in a collection

    Args:
        mongo_collection (Collection): pymongo collection object

    Returns:
        List[dict]: A list of documents in the collection
    """
    # Find all documents in the collection and return as a list
    return list(mongo_collection.find({}))
