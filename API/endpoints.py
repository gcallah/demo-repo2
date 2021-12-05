"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.data as db

app = Flask(__name__)
api = Api(app)

HELLO = 'Hola'
WORLD = 'mundo'


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO: WORLD}


@api.route('/rooms/list')
class ListRooms(Resource):
    """
    This endpoint returns a list of all rooms.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all chat rooms.
        """
        rooms = db.get_rooms()
        if rooms is None:
            raise (wz.NotFound("Chat room db not found."))
        else:
            return rooms


@api.route('/rooms/create/<roomname>')
class CreateRoom(Resource):
    """
    This class supports adding a chat room.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, roomname):
        """
        This method adds a room to the room db.
        """
        ret = db.add_room(roomname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Chat room db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Chat room name already exists."))
        else:
            return f"{roomname} added."


@api.route('/rooms/delete/<roomname>')
class DeleteRoom(Resource):
    """
    This class enables deleting a chat room.
    While 'Forbidden` is a possible return value, we have not yet implemented
    a user privileges section, so it isn't used yet.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.FORBIDDEN,
                  'Only the owner of a room can delete it.')
    def post(self, roomname):
        """
        This method deletes a room from the room db.
        """
        ret = db.del_room(roomname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Chat room {roomname} not found."))
        else:
            return f"{roomname} deleted."


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    @api.response(HTTPStatus.OK, 'Success')
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/users/list')
class ListUsers(Resource):
    """
    This endpoint returns a list of all users.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self):
        """
        Returns a list of all users.
        """
        users = db.get_users()
        if users is None:
            raise (wz.NotFound("User db not found."))
        else:
            return users


@api.route('/users/create/<username>')
class CreateUser(Resource):
    """
    This class supports adding a user to the chat room.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    @api.response(HTTPStatus.NOT_ACCEPTABLE, 'A duplicate key')
    def post(self, username):
        """
        This method adds a user to the chatroom.
        """
        """
        This method adds a room to the room db.
        """
        ret = db.add_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("User db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User name already exists."))
        return f"{username} added."
