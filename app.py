from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask('_name_')

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return hello_world

@app.route('/add', methods=['POST'])
def add_user():
    user = request.json
    mongo.db.users.insert_These({"name":"sahil","email":"sahilkadam2205@gmail.com"})
    return add_user

@app.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find())
    return get_users
    
if __name__ == '__main__':
    app.run(debug=True)
