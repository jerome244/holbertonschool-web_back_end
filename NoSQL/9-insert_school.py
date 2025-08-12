#!/usr/bin/env python3
""" Pymongo """

def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in the collection based on kwargs

    Args:
        mongo_collection (object): The pymongo collection object.
        **kwargs: Key-value pairs representing the fields of the document to be inserted.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)  # Inserts the document into the collection.
    return result.inserted_id  # Returns the _id of the newly inserted document.
