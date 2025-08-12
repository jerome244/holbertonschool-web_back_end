#!/usr/bin/env python3
"""List all databases in MongoDB"""

import pymongo

def list_databases():
    """Lists all databases in MongoDB"""
    # Connect to the MongoDB server (localhost by default)
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # List all database names
    databases = client.list_database_names()

    # Print all database names
    for db in databases:
        print(db)

if __name__ == "__main__":
    list_databases()
