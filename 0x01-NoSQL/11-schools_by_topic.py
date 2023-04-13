#!/usr/bin/env python3
""" 
    a module that returns all docs
    that match the topic
"""


def schools_by_topic(mongo_collection, topic):
    """
        The function used to find the topics
        Args:
            :mongo_collection: The collection we want to query
            :topic: what we use to query the mongo_collection
    """
    return mongo_collection.find({"topics": topic})
