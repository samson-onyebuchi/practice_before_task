from flask import Flask, request
from pymongo import MongoClient
from mongoDB_URL import mongodb_url


app = Flask(__name__)
client = MongoClient(mongodb_url())
db = client["mydatabase"]
users_collection = db["Test"]
@app.route('/')
def home():
    return "welcome to home page"
@app.route('/register', methods=['POST'])
def register_user():
    phone_number = request.form['phone_number']
    password = request.form['password']

    user_data = {
    'phone_number': phone_number,
    'password': password
    }

    result = users_collection.insert_one(user_data)

    if result.inserted_id:
        return "User registered successfully."
    else:
        return "Error registering user."

if __name__ == "__main__":
    app.run(debug=True)