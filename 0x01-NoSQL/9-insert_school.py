#!/usr/bin/env python3
"""python function"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert new document"""
    return mongo_collection.insert(kwargs)
