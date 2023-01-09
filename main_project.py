from flask import Flask, request
from pymongo import MongoClient
import bcrypt
from mongoDB_URL import mongodb_url

app = Flask(__name__)
client = MongoClient(mongodb_url())
db = client["mydatabase"]
users_collection = db["Test"]

@app.route('/')
def home():
    return "Welcome to the page"
@app.route('/register', methods=["POST"])
def register_user():
    phone_number = request.json("phone_number")
    pin = request.json("pin")

    hashed = bcrypt.hashpw(pin.encode('utf-8'), bcrypt.gensalt())
    user = {"phone_nuber":phone_number, "pin":hashed}

    users_collection.insert_one(user)
    return "Suuccesful message"


def validate_pin(phone_number, pin):
  # Find the user with the matching phone number
  user = users_collection.find_one({"phone_number": phone_number})
  
  # If a user with the specified phone number was found
  if user:
    # Check if the provided PIN matches the user's stored PIN
    if user["pin"] == pin:
      return True
    else:
      return False
  else:
    return False


def lock_account(user_id):
    # Update the user document to set the "account_status" field to "locked"
    users_collection.update_one({"_id": user_id}, {"$set": {"account_status": "locked"}})

    # Close the connection
client.close()

if __name__ == "__main__":
    app.run()