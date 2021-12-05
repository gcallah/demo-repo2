"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os
import pymongo as pm
import bson.json_util as bsutil

DEMO_HOME = os.environ["DEMO_HOME"]
TEST_MODE = os.environ.get("TEST_MODE", 0)

if TEST_MODE:
    DB_DIR = f"{DEMO_HOME}/db/test_dbs"
else:
    DB_DIR = f"{DEMO_HOME}/db"

ROOM_COLLECTION = f"{DB_DIR}/rooms.json"
USER_COLLECTION = f"{DB_DIR}/users.json"

DB_NAME = "chatDB"
ROOMS = "rooms"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2

# we'll begin cutting over to mongo!
client = pm.MongoClient()
print(client)


def write_collection(perm_version, mem_version):
    """
    Write out the in-memory data collection in proper DB format.
    """
    with open(perm_version, 'w') as f:
        json.dump(mem_version, f, indent=4)


def read_collection(perm_version):
    """
    A function to read a colleciton off of disk.
    """
    print(f"{perm_version=}")
    try:
        with open(perm_version) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print(f"{perm_version} not found.")
        return None


def fetch_all(collect_nm):
    all_docs = []
    for doc in client[DB_NAME][collect_nm].find():
        print(doc)
        all_docs.append(json.loads(bsutil.dumps(doc)))
    return all_docs


def get_rooms():
    """
    A function to return a dictionary of all rooms.
    """
    # return read_collection(ROOM_COLLECTION)
    return fetch_all(ROOMS)
    # rooms = []
    # for room in client[DB_NAME][ROOMS].find():
    #     print(room)
    #     rooms.append(json.loads(bsutil.dumps(room)))
    # return rooms


def room_exists(roomname):
    rooms = get_rooms()
    return roomname in rooms


def del_room(roomname):
    """
    Delete roomname from the db.
    """
    if not room_exists(roomname):
        return NOT_FOUND
    return OK


def add_room(roomname):
    """
    Add a room to the room database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    rooms = get_rooms()
    if rooms is None:
        return NOT_FOUND
    elif roomname in rooms:
        return DUPLICATE
    else:
        rooms[roomname] = {"num_users": 0}
        write_collection(ROOM_COLLECTION, rooms)
        return OK


def get_users():
    """
    A function to return a dictionary of all users.
    """
    return read_collection(USER_COLLECTION)


def add_user(username):
    """
    Add a user to the user database.
    Until we are using a real DB, we have a potential
    race condition here.
    """
    users = get_users()
    if users is None:
        return NOT_FOUND
    elif username in users:
        return DUPLICATE
    else:
        users[username] = {}
        write_collection(USER_COLLECTION, users)
        return OK
