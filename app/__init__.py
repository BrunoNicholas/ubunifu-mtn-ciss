import os
from flask import Flask, jsonify

from .vroutes.views_v1 import system_app

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'CI-CIS')

# register a blueprint for the version
# with the API standard
# If there is a new version, the views file will be different
# and the blueprint will be updated to a new line
# such as /api/v2

app.register_blueprint(system_app, url_prefix="/api/v1")


# capturing error of load
@app.route('/', methods=['GET'])
def welcome():
    data = {
        'info': 'MTN CS CIS, please follow the app documentation to proceed',
        'message': 'To use the API, update the url by adding /api',
        'status': 206
    }
    return jsonify(data), 206


@app.route('/api', methods=['GET'])
@app.route('/api/', methods=['GET'])
def api_route():
    data = {
        'info': 'you are close, now add a version to proceed (v1,v2,...)',
        'status': 206
    }
    return jsonify(data), 206


# Handling of route errors
@app.errorhandler(400)
def bad_request(error):
    """
    Gives error message when any bad requests are made.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 400}), 400


@app.errorhandler(404)
def not_found(error):
    """
    Gives error message when any invalid url are requested.
    Args:
        error (string): 
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 404}), 404


@app.errorhandler(403)
def not_allowed(error):
    """
    Gives error message when a resource is restricted from the user access.
    Args:
        error (string): 
    Returns:
        Error message.
    """
    print(error)
    return jsonify({'error': '{}!'.format(error), 'status': 403}), 403


@app.errorhandler(415)
def handle_unsupported_media_type(error):
    return jsonify({'error': 'Unsupported Media Type - Use JSON', 'status': 415}), 415


@app.errorhandler(500)
def special_exception_handler(error):
    return jsonify({'error': 'Internal Server Error or Database connection failed!', 'status': 500}), 500
