#!/usr/bin/env python3
"""python function"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """return list of schools"""
    return mongo_collection.find({"topics": topic})
