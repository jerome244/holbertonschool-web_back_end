#!/usr/bin/env python3
"""Script to retrieve statistics from Nginx logs in MongoDB"""

from pymongo import MongoClient

def log_stats():
    """Prints statistics from the Nginx logs in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get total number of logs in the collection
    total_logs = collection.count_documents({})

    # Display total logs
    print(f"{total_logs} logs")

    # Display HTTP methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Display count of logs with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
