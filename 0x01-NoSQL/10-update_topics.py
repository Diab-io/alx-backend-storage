#!/usr/bin/env python3
""" 
    Changes the topics of a document
    based on the name specified
"""


def update_topics(mongo_collection, name, topics):
    """ The function that implements updating by name """
    return mongo_collection.update_many({"name": name}, {"$set":{"topics": topics}})
