"""
Get used to pymongo!
"""
import pymongo as pm

DB_NAME = 'testDB'
COLLECT_NAME = 'email'


client = pm.MongoClient()
print(f"{client=}")

this_collect = client[DB_NAME][COLLECT_NAME]

insert_ret = client[DB_NAME][COLLECT_NAME].insert_many([{'filter_nm': 'bar1'},
                                                       {'filter_nm': 'bar2'},
                                                       {'filter_nm': 'bar3'},
                                                       {'filter_nm': 'bar4'},
                                                       {'filter_nm': 'bar5'}])
insert_ret = this_collect.insert_one({'trees': 'yellow leaves'})
print(f"{insert_ret=}")

docs = client[DB_NAME][COLLECT_NAME].find()
print(f"{docs=}")
for doc in docs:
    print(f"{doc=}")

doc = client[DB_NAME][COLLECT_NAME].find_one({'trees': 'yellow leaves'})
print(f"find one = {doc=}")

doc = client[DB_NAME][COLLECT_NAME].delete_many({'foo': 'bar'})
print(f"find one = {doc=}")

docs = client[DB_NAME][COLLECT_NAME].find()
for doc in docs:
    print(f"{doc=}")
