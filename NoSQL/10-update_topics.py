#!/usr/bin/env python3
"""Function to update topics of a school in MongoDB"""

def update_topics(mongo_collection, name, topics):
    """Updates the topics of a school based on its name

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to set for the school.
    """
    mongo_collection.update_one(
        {"name": name}, 
        {"$set": {"topics": topics}}
    )
