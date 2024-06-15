#!/usr/bin/env python3
"""python function"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """change all topics"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topic}})
