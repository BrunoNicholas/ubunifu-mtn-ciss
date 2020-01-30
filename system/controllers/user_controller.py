from flask import jsonify, request

from ..models.data.userResource import UsersData
from ..models.user import User


class UserController:
    def __init__(self):
        self.sys_users = UsersData()

    def index(self):
        """ this function returns all users """
        try:
            return jsonify(self.sys_users), 200

        except IndexError:
            return jsonify({'error': 'There is an internal problem'}), 500

