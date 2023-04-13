#!/usr/bin/env python3
""" inserts a new document in the collection based off kwargs """


def insert_school(mongo_collection, **kwargs):
    """ inserts a document to the provided collection """
    doc_data = mongo_collection.insert_one(kwargs)
    return doc_data.inserted_id
