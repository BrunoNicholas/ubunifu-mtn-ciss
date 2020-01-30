import os
import click
import unittest

from system import app
import json

TEST_DB = 'test.db'


@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    pass

class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        :return:
        """
        app.config.from_object('app.config.TestingConfig')
        return app

    def setUp(self):
        """
        Create the database
        :return:
        """
        self.users = [
            {
                "user_id":234,
                "msisdn":256781000000
            },
            {
                "user_id":827,
                "msisdn":256772111111
            }
        ]
        # db.create_all()
        # db.session.commit()
        pass

    def tearDown(self):
        """
        Drop the database tables and also remove the session
        :return:
        """
        # db.session.remove()
        # db.drop_all()
        pass

    def register_user(self, msisdn, password):
        """
        Helper method for registering a user with dummy data
        :return:
        """
        # return self.user.post(
        #     'v1/auth/register',
        #     content_type='application/json',
        #     data=json.dumps(dict(msisdn=msisdn, password=password)))
        pass

    def get_user_token(self):
        """
        Get a user token
        :return:
        """
        # auth_res = self.register_user('256781000000', '123456')
        # return json.loads(auth_res.data.decode())['auth_token']
        pass
