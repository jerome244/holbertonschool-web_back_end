#!/usr/bin/env python3
"""Function to get schools by topic"""

def schools_by_topic(mongo_collection, topic):
    """Returns a list of schools having a specific topic

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        List[dict]: A list of schools (documents) having the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
