#!/usr/bin/env python3
"""python function"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """return all students sorted"""
    pipeline = mongo_collection.aggregate([
        {
            "$group": {
                "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])
    return pipeline
