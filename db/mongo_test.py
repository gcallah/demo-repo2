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
=======
Get used to pymongo!
"""
import db.db_connect as dbc

COLLECT_NAME = 'email'


client = dbc.get_client()
print(f"{client=}")

this_collect = client[dbc.db_nm][COLLECT_NAME]

insert_ret = this_collect.insert_many([{'filter_nm': 'bar1'},
                                      {'filter_nm': 'bar2'},
                                      {'filter_nm': 'bar3'},
                                      {'filter_nm': 'bar4'},
                                      {'filter_nm': 'bar5'}])
insert_ret = this_collect.insert_one({'trees': 'yellow leaves'})
print(f"{insert_ret=}")

docs = client[dbc.db_nm][COLLECT_NAME].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = client[dbc.db_nm][COLLECT_NAME].find_one({'trees': 'yellow leaves'})
print(f"find one = {doc=}")

doc = client[dbc.db_nm][COLLECT_NAME].delete_many({'foo': 'bar'})
print(f"find one = {doc=}")

docs = client[dbc.db_nm][COLLECT_NAME].find()
for doc in docs:
    print(f"{doc=}")
