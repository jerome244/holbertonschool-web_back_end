#!/usr/bin/env python3
"""Script that creates or uses the database my_db"""

from pymongo import MongoClient

def create_or_use_database():
    # Connect to MongoDB (default localhost:27017)
    client = MongoClient('mongodb://localhost:27017/')
    
    # Switch to or create the 'my_db' database
    db = client.my_db
    
    # Show the current database name (this will display 'my_db')
    print(f"Switched to db {db.name}")

if __name__ == "__main__":
    create_or_use_database()
