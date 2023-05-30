from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    message = {'message': 'Hello, World!'}
    return jsonify(message)

@app.route('/users', methods=['GET'])
def get_users():
    users = read_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    user = request.get_json()
    users = read_users()
    users.append(user)
    write_users(users)
    return jsonify(user), 201

def read_users():
    with open('data/users.json', 'r') as file:
        users = json.load(file)
    return users

def write_users(users):
    with open('data/users.json', 'w') as file:
        json.dump(users, file)

if __name__ == '__main__':
    app.run()
