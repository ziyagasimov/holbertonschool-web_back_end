from pymongo import MongoClient

def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    # Connect to the MongoDB instance
    # Assuming default host and port
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the specific database and collection
    db = client.logs
    collection = db.nginx

    # 1. Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Stats by Method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    
    for method in methods:
        count = collection.count_documents({"method": method})
        # Note: The prompt specifies a tabulation before each line
        print(f"\tmethod {method}: {count}")

    # 3. Status Check (method=GET and path=/status)
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
