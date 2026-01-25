#!/usr/bin/env python3
""" 12-log_stats.py """
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to the MongoDB instance (default host and port)
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specific database and collection
    collection = client.logs.nginx

    # 1. Display total number of documents
    # Output: x logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Display stats by Method
    # Output: Methods:
    #         method <METHOD>: <count>
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = collection.count_documents({"method": method})
        # The prompt specifies a tabulation before each line
        print(f"\tmethod {method}: {count}")

    # 3. Display Status Check count
    # Output: x status check
    # Filter: method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")
