import pymongo
import bcrypt
from mongoDB_URL import mongodb_url

# Connect to the MongoDB server
client = pymongo.MongoClient(mongodb_url())

# Select the database and collection to use
db = client["mydatabase"]
users_collection = db["Test"]

# Get the phone number and password from the user
phone_number = input("Enter your phone number: ")
pin = input("Enter your password: ")

# Create a new user document with the phone number and password

# Insert the new user document into the collection

hashed = bcrypt.hashpw(pin.encode('utf-8'), bcrypt.gensalt())
new_user = {
    "phone_number": phone_number,
    "pin": pin
}

users_collection.insert_one(new_user)
print("Registration was successful")


# Close the connection to the MongoDB server
client.close()