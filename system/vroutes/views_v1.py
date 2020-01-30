from flask import Blueprint, jsonify, request, abort

# from ..controllers.user_controller import UserController


JSON_MIME_TYPE = 'application/json'

system_app = Blueprint('system_app', __name__)

OTT_Bundles = [
    {
        'bundle_id': 1101,
        'bundle_name': 'Daily OTT at 200/-',
        'validity': '24 Hours',
        'status': 'available'
    },
    {
        'bundle_id': 1102,
        'bundle_name': 'Weekly OTT at 1400/-',
        'validity': '7 Days',
        'status': 'available'
    },
    {
        'bundle_id': 1103,
        'bundle_name': 'Monthly OTT at 6000/-',
        'validity': '30 Days',
        'status': 'available'
    },
    {
        'bundle_id': 1104,
        'bundle_name': 'Quarterly OTT at 18000/-',
        'validity': '4 Months',
        'status': 'available'
    },
    {
        'bundle_id': 1105,
        'bundle_name': 'Annual OTT at 73000/-',
        'validity': '12 Months',
        'status': 'available'
    }
]


# first success on load
@system_app.route('/', methods=['GET'])
def index():
    data = {
        'info': 'Welcome! Please follow the documentation to proceed.',
        'status': 200
    }
    return jsonify(data), 200


# first success on load
@system_app.route('/pulse', methods=['GET'])
def pulse_menu():
    data = {
        'error': 'The pulse resource is not yet fully open for use but some modules are open. Partly Restricted Access',
        'status': 206
    }
    return jsonify(data), 206


# returns the JSON response of OTT Bundles
@system_app.route('/pulse/ott', methods=['GET', 'POST'])
def ott_menu():
    data = OTT_Bundles
    return jsonify(data), 202


# returns JSON response of the pulse bundles
@system_app.route('/pulse/data-bundles', methods=['GET', 'POST'])
def pulse_data():
    abort(403)


# returns the voice bundle packages
@system_app.route('/pulse/voice-bundles', methods=['GET', 'POST'])
def pulse_voice():
    abort(403)


# returns the available freebies
@system_app.route('/pulse/freebies', methods=['GET', 'POST'])
def pulse_freebies():
    abort(403)


# to check remaining data
@system_app.route('/balance/data', methods=['GET', 'POST'])
def balance_data():
    abort(403)


# to check remaining data send
@system_app.route('/balance/voice', methods=['GET', 'POST'])
def balance_voice():
    abort(403)


# to crack the egg
@system_app.route('/crack-the-egg', methods=['GET', 'POST'])
def crack_egg():
    if request.method == 'POST':
        if not request.is_json:
            abort(415)

        if request.json['msisdn'] is None:
            data = {
                'error': 'The user\'s phone number is not submitted',
                'status': 406
            }
            return jsonify(data), 406

        data = {
            'info': 'Congratulations! You cracked the Egg.',
            'reward': '150 MBs on {}'.format(request.json['msisdn']),
            'validity': '24 Hours'
        }
        return jsonify(data), 206

    data = {
        'info': 'You are set to crack the egg!',
        'status': 200
    }
    return jsonify(data), 200
