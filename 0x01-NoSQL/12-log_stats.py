#!/usr/bin/env python3

"""module list nginx stats"""

from typing import List
from pymongo import MongoClient

if __name__ == "__main__":
    # Establish connection
    client: MongoClient = MongoClient(host="localhost", port=27017)
    # Select the database
    db = client["logs"]
    # Select the collection
    collection = db.nginx
    total_logs: int = collection.count_documents({})
    print("{} logs".format(total_logs))
    status: int = collection.count_documents({"path": "/status"})
    print("Methods:")
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count: int = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    print(f"{status} status check")
