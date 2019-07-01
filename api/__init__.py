from flask import (
    Flask,
    jsonify,
    request,
    make_response
)


app = Flask(__name__)


def __create_mock_user(uid, name):
    return {
        'id': uid,
        'name': name
    }


@app.route('/users', methods=['GET'])
def list_users():
    # request.args.param_mame
    # request.form.param_name
    # request.data - raw
    # request.headers['Authorization']
    users = [__create_mock_user(i, 'User') for i in range(5)]
    return jsonify(data=users), 200


@app.route('/users', methods=['POST'])
def create_user():
    user = __create_mock_user(1, 'Armando')
    resp = make_response(jsonify(data=user), 201)
    # resp.headers.add('X-My-Header', 'xxx')
    return resp


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = __create_mock_user(1, 'Armando')
    return jsonify(data=user), 201


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return '', 204


def run_webserver(port):
    app.run(host='0.0.0.0', port=port)
