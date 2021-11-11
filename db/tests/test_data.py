"""
This file holds the tests for db.py.
"""

from unittest import TestCase, skip
# import random

import db.data as db


class DBTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_users(self):
        """
        Can we fetch user db?
        """
        users = db.get_users()
        self.assertIsInstance(users, dict)
