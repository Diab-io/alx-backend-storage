#!/usr/bin/env python3
""" lists all documents in the collection of our mongo db """

import pymongo


def list_all(mongo_collection):
    """ checks the collection and displays all docs """
    if (mongo_collection.find()):
        return mongo_collection.find()
    else:
        return []
