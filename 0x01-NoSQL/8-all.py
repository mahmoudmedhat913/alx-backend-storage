#!/usr/bin/env python3
"""python function"""
import pymongo


def list_all(mongo_collection):
    """return listof all docs"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
