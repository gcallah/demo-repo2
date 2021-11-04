"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import os

DEMO_HOME = os.environ["DEMO_HOME"]

ROOMS_DB = f"{DEMO_HOME}/db/rooms.json"

OK = 0
NOT_FOUND = 1
DUPLICATE = 2


def write_rooms(rooms):
    with open(ROOMS_DB, 'w') as f:
        json.dump(rooms, f, indent=4)


def get_rooms():
    """
    A function to return all chat rooms.
    """
    try:
        with open(ROOMS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print("Rooms db not found.")
        return None


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
        write_rooms(rooms)
        return OK
