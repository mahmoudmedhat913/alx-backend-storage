#!/usr/bin/env python3
"""python function"""


def top_students(mongo_collection):
    """return all students sorted"""
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ])

    return top_student
