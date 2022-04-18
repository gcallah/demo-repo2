"""
This program is written to port text JSON files into Mongo collections.
It assumes the JSON files have the structure:
    {
        "some_fld1": { some more fields },
        "some_fld2": { some more fields },
        .
        .
        .
        "some_fldN": { some more fields },
    }
It assumes that cause that's what we've been using!
"""
# import sys
# import json
import pymongo as pm


client = pm.MongoClient()
print(client)

# db = client["ChatDB"]
# print(db)
# collect_nm = sys.argv[2]
# print(f"{collect_nm=}")
# collection = db[collect_nm]
