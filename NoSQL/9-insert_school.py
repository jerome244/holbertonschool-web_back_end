#!/usr/bin/env python3
""" Insert a new document in a collection """

from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs):
    """Insert a new document in the collection using keyword arguments

    Args:
        mongo_collection (Collection): pymongo collection object
        kwargs: fields of the document to be inserted

    Returns:
        The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
