"""
This file holds the tests for db.py.
"""

from unittest import TestCase
# import random

# import pymongo as pm

import db.data as db
from db_connect import client, db_nm, get_client

KNOWN_USER = "Known user"
ABSENT_USER = "Not in DB!"


client = get_client()  # noqa F811
if client is None:
    print("Failed to connect to MongoDB.")
    exit(1)


class DBTestCase(TestCase):
    def setUp(self):
        client[db_nm][db.USERS].insert_one({db.USER_NM: KNOWN_USER})

    def tearDown(self):
        client[db_nm][db.USERS].delete_many({})
        # client[db_nm][db.ROOMS].delete_many({})

    def test_user_exists(self):
        users = client[db_nm][db.USERS]
        print(f'{users.count_documents({})=}')
        self.assertTrue(db.user_exists(KNOWN_USER))
        self.assertFalse(db.user_exists(ABSENT_USER))

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = db.get_users()
        self.assertIsInstance(users, list)
        found = False
        for user in users:
            if user[db.USER_NM] == KNOWN_USER:
                found = True
        self.assertTrue(found)

    def test_get_rooms(self):
        """
        Can we fetch user db?
        """
        rooms = db.get_rooms()
        self.assertIsInstance(rooms, list)
