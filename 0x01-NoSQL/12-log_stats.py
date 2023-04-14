#!/usr/bin/env python3
"""
    this script is used to display the stats
    of some nginx logs
    database: logs
    collection: nginx
"""

from pymongo import MongoClient


def nginx_stats(mongo_collection):
    """
        :nginx_stats: provides stats about logs of the nginx collection
    """
    num_of_docs = mongo_collection.count_documents({})
    print(f"{num_of_docs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f'\tmethod {method}: {mongo_collection.count_documents({"method": method})}')
    
    status = mongo_collection.count_documents({'method': 'Get', 'path': '/status'})
    print(f"{status} status check")


if __name__ == "__main__":
    client = MongoClient()
    db = client.log
    collection = db.nginx
    nginx_stats(collection)
