from flask import Flask, jsonify, request
from flask_cors import CORS
from api import API
api = API()

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():

    response = {
        "message": "API works!"
    }
    return jsonify(response)

@app.route('/items', methods =['GET'])
def get_items():
    try:
        response = {
            "message": "Data from some API",
            "data": api.get_items(),
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed to get data'}), 400

@app.route('/items/<username>', methods =['GET'])
def get_items_user(username):
    try:
        response = {
            "message": "Data from some API",
            "data": api.get_items(username),
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed to get data'}), 400

@app.route('/items', methods =['POST'])
def add_item():
    try:
        item = request.json['item']
        response = {
            "message": "Added item!",
            'item': api.add_item(item)
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400


@app.route('/items/<id>', methods =['DELETE'])
def delete_item(id):
    try:
        api.delete_item(id)
        response = {
            "message": "Deleted item!"
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": 'Failed'}), 400

@app.route('/users', methods =['GET'])
def get_users():
    try:
        
        response = {
            "message": "All users",
            "users": api.get_users(),
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    
@app.route('/users', methods =['POST'])
def add_user():
    try:
        username = request.json['username']
        password = request.json['password']
        response = {
            "message": "New User",
            "user": api.create_user(username, password)
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    
@app.route('/users/login', methods =['POST'])
def get_user():
    try:
        username = request.json['username']
        password = request.json['password']
        response = {
            "user": api.read_user(username, password),
            "message": "Welcome!",
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400

@app.route('/users/<username>', methods =['DELETE'])
def delete_user(username):
    try:
        api.delete_user(username)
        response = {
            "message": "User deleted!"
        }
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 400
    
    
if __name__ == "__main__":
    app.run(debug=True)