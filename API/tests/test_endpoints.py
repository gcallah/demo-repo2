"""
This file holds the tests for endpoints.py.
"""

from unittest import TestCase, skip
from flask import Flask
from flask_restx import Resource, Api

import random

import API.endpoints as ep
import db.data as db

HUGE_NUM = 10000000000000  # any big number will do!


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)

    def test_create_user(self):
        """
        See if we can successfully create a new user.
        Post-condition: user is in DB.
        """
        assert True

    def test_create_room(self):
        """
        See if we can successfully create a new room.
        Post-condition: room is in DB.
        """
        ep.TEST_ROOM_FIELDS[ep.ROOM_NAME] = new_entity_name('room')
        response = ep.app.test_client().post('/rooms/create', json=ep.TEST_ROOM_FIELDS)
        print(f'post {response=}')
        self.assertEqual(response.status_code, 200)
        rooms = db.get_rooms_as_dict()
        self.assertIn('foo', rooms)

    def test_list_rooms1(self):
        """
        Post-condition 1: return is a list.
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, list)
