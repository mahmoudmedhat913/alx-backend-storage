#!/usr/bin/env python3
"""python function"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """return all students sorted"""
    pipeline = mongo_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "averageScore": {"$avg": "$score"}
        }
    },
    {
        '$sort': {'averageScore': -1}
    }
])
    return pipeline
