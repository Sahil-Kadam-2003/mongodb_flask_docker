from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    
    if request.is_json:
        json = request.get_json()
        name = json.get('name')
        email = json.get('email')
        pwd = json.get('pwd')

        
        if name and email and pwd:
            mongo.db.user.insert_one({'name': name, 'email': email, 'pwd': pwd})
            return jsonify({"message": "User added successfully"}), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
