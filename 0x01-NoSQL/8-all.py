#!/usr/bin/env python3
"""lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """ function that lists all documents"""
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]
